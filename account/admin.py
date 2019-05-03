from django.contrib import admin
from .models import UserProfile, Membership


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'nama_lengkap', 'no_handphone', 'bidang', 'role']}),
        ('Informasi Guru', {'fields': ['guru_pembimbing', 'no_handphone_guru']}),
        ('Informasi Sekolah', {'fields': ['asal_sekolah', 'kota', 'provinsi']}),
    ]
    list_display = ['user',
                    'nama_lengkap',
                    'no_handphone',
                    'bidang',
                    'role',
                    'guru_pembimbing',
                    'no_handphone_guru',
                    'asal_sekolah',
                    'kota',
                    'provinsi']
    list_filter = ['bidang', 'role']
    search_fields = ['nama_lengkap', 'asal_sekolah', 'user__username', 'kota', 'provinsi']

admin.site.register(UserProfile, UserProfileAdmin)



class MembershipAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['userprofile', 'event', 'confirmed']}),
    ]
    actions = ['confirm_membership']
    list_filter = ['confirmed', 'userprofile__bidang', 'userprofile__role']
    list_display = ('id', 'get_username', 'userprofile', 'get_asal_sekolah', 'get_role', 'get_bidang', 'event', 'confirmed')
    search_fields = ['userprofile__user__username', 'userprofile__nama_lengkap', 'userprofile__asal_sekolah', 'userprofile__kota', 'userprofile__kota', 'userprofile__provinsi',  'event__nama_event']

    def confirm_membership(self, request, queryset):
        queryset.update(confirmed=True)
        self.message_user(request, "%s Keanggotaan berhasil dikonfirmasi." % queryset.count())

admin.site.register(Membership, MembershipAdmin)
