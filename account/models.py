from django.db import models
from django.contrib.auth.models import User
from pelatihanonline.constants import SUBJECT_CHOICES, ROLE_CHOICES
from program.models import Event


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    events = models.ManyToManyField(Event, through='Membership')

    # data wajib
    no_handphone = models.CharField(max_length=15)
    bidang = models.CharField(max_length=3,
                              choices=SUBJECT_CHOICES,
                              blank=False,
                              help_text="Bidang hanya dapat diatur sekali di awal.")
    role = models.CharField(max_length=3,
                            choices=ROLE_CHOICES,
                            blank=False,
                            default="SIS",
                            help_text="Role hanya dapat diatur sekali di awal. Nilai guru tidak disertakan dalam ranking.")

    asal_sekolah = models.CharField(max_length=100)
    kota = models.CharField(max_length=100)
    provinsi = models.CharField(max_length=100)

    # data opsional
    guru_pembimbing = models.CharField(max_length=100,
                                       default="",
                                       blank=True,
                                       help_text="Opsional")
    no_handphone_guru = models.CharField(max_length=15,
                                         default="",
                                         blank=True,
                                         help_text="Opsional")

    def __str__(self):
        return self.nama_lengkap



class Membership(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return " - ".join([self.event.nama_event,
                           self.userprofile.nama_lengkap,
                           str(self.confirmed)])

    def get_username(self):
        return self.userprofile.user.username

    get_username.short_description = 'Username'


    def get_asal_sekolah(self):
        return self.userprofile.asal_sekolah

    get_asal_sekolah.short_description = 'Asal Sekolah'


    def get_role(self):
        return self.userprofile.get_role_display()

    get_role.short_description = 'Role'

    def get_bidang(self):
        return self.userprofile.get_bidang_display()

    get_bidang.short_description = 'Bidang'
