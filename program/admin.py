from django.contrib import admin
from django.http import HttpResponse
from .models import Program, NomorPaket, Event, Paket
from soal.models import Submission
from account.models import Membership
from pelatihanonline.constants import SUBJECT_CHOICES
from openpyxl import Workbook



class NomorPaketInline(admin.TabularInline):
    model = NomorPaket
    extra = 0

class ProgramAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nama_program']}),
    ]
    inlines = [NomorPaketInline]
    actions = ['generate_report']
    list_display = ('nama_program', 'event_count')
    search_fields = ['nama_program']

    def generate_report(self, request, queryset):
        program = queryset[0]
        nomors = program.nomorpaket_set.all().order_by('kode')
        wb = Workbook(write_only=True)
        header = ['Nama Lengkap',
                  'Bidang',
                  'Asal Sekolah',
                  'Kota',
                  'Provinsi']
        header = header + [nomor.kode for nomor in nomors]
        header.append('Total')

        for bidang in SUBJECT_CHOICES:
            ws = wb.create_sheet(title=bidang[1])
            ws.append(header)
            memberships = Membership.objects.filter(userprofile__bidang=bidang[0],
                                                    event__program=program,
                                                    confirmed=True)
            for member in memberships:
                userprofile = member.userprofile
                data = [userprofile.nama_lengkap,
                        userprofile.get_bidang_display(),
                        userprofile.asal_sekolah,
                        userprofile.kota,
                        userprofile.provinsi]
                total = 0
                for nomor in nomors:
                    nilai = '0'
                    try:
                        submission = Submission.objects.get(paket__nomor_paket=nomor,
                                                            userprofile=userprofile,
                                                            bidang=bidang[0])
                        total = total + submission.nilai
                        nilai = str(submission.nilai)
                    except:
                        nilai = ''
                    data.append(nilai)
                data.append(str(total))
                ws.append(data)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename={}.xlsx'.format(program.nama_program)
        wb.save(response)
        return response


admin.site.register(Program, ProgramAdmin)



class PaketInline(admin.TabularInline):
    model = Paket
    extra = 0

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nama_event', 'program', 'link_panduan', 'aktif']}),
        ('Jadwal', {'fields': ['jadwal', 'waktu_buka', 'waktu_mulai', 'waktu_selesai', 'waktu_download']}),
    ]
    actions = ['activate_program', 'deactivate_program']
    inlines = [PaketInline]
    list_filter = ['aktif']
    list_display = ('nama_event', 'link_panduan', 'aktif', 'paket_count', 'status')
    search_fields = ['nama_event']

admin.site.register(Event, EventAdmin)



class PaketAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nama_paket', 'nomor_paket', 'event', 'bundel_soal']}),
        ('Jadwal', {'fields': ['open_time', 'close_time']}),
    ]
    list_display = ('nama_paket', 'event', 'bundel_soal', 'open_time_format', 'close_time_format',)
    search_fields = ['nama_paket']

admin.site.register(Paket, PaketAdmin)
