import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import BundelSoal, Soal, Submission


class SoalInline(admin.TabularInline):
    model = Soal
    extra = 0
    exclude = ['no1', 'no2', 'no3', 'no4', 'no5', 'no6', 'no7', 'no8', 'no9', 'no10',
               'no11', 'no12', 'no13', 'no14', 'no15', 'no16', 'no17', 'no18', 'no19', 'no20',
               'no21', 'no22', 'no23', 'no24', 'no25', 'no26', 'no27', 'no28', 'no29', 'no30']


class BundelSoalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nama_bundel_soal']}),
    ]
    inlines = [SoalInline]
    list_display = ('nama_bundel_soal', 'soal_count')
    search_fields = ['nama_bundel_soal']

admin.site.register(BundelSoal, BundelSoalAdmin)



class SoalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nama_soal', 'bundel_soal', 'bidang', 'judul_materi']}),
        ('Soal Solusi', {'fields': ['file_soal', 'file_solusi']}),
        ('Jawaban', {'fields': [('no1', 'no11', 'no21'),
                                ('no2', 'no12', 'no22'),
                                ('no3', 'no13', 'no23'),
                                ('no4', 'no14', 'no24'),
                                ('no5', 'no15', 'no25'),
                                ('no6', 'no16', 'no26'),
                                ('no7', 'no17', 'no27'),
                                ('no8', 'no18', 'no28'),
                                ('no9', 'no19', 'no29'),
                                ('no10', 'no20', 'no30')]}),
    ]
    list_display = ['nama_soal', 'bidang', 'judul_materi', 'file_soal', 'file_solusi']
    list_filter = ['bidang']
    search_fields = ['nama_soal']

admin.site.register(Soal, SoalAdmin)



class SubmissionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['userprofile', 'paket', 'bidang']}),
        ('Nilai', {'fields': ['graded', 'nilai']}),
        ('Jawaban', {'fields': [('no1', 'no11', 'no21'),
                                ('no2', 'no12', 'no22'),
                                ('no3', 'no13', 'no23'),
                                ('no4', 'no14', 'no24'),
                                ('no5', 'no15', 'no25'),
                                ('no6', 'no16', 'no26'),
                                ('no7', 'no17', 'no27'),
                                ('no8', 'no18', 'no28'),
                                ('no9', 'no19', 'no29'),
                                ('no10', 'no20', 'no30')]})
    ]
    actions = ['grade_submissions', 'export_submissions']
    list_display = ['id', 'userprofile', 'paket', 'bidang', 'graded', 'nilai']
    list_filter = ['bidang', 'graded', ('paket', admin.RelatedOnlyFieldListFilter)]
    search_fields = ['userprofile__nama_lengkap', 'userprofile__user__username', 'userprofile__asal_sekolah']

    def grade_submissions(self, request, queryset):
        for obj in queryset:
            obj.grade()
        self.message_user(request, "%s Jawaban berhasil dinilai ulang." % queryset.count())

    def export_submissions(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=result.csv'
        writer = csv.writer(response)
        writer.writerow(['Nama Lengkap', 'Asal Sekolah', 'Paket', 'Bidang', 'Nilai'])
        for obj in queryset:
            row = writer.writerow([obj.userprofile.nama_lengkap, obj.userprofile.asal_sekolah, obj.paket, obj.get_bidang_display(), obj.nilai])
        return response

admin.site.register(Submission, SubmissionAdmin)
