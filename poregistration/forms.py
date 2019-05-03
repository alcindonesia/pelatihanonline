from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import UserProfile
from pelatihanonline.constants import SUBJECT_CHOICES, ROLE_CHOICES


class UserCreateForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'validate',}))
    nama_lengkap = forms.CharField(label='Nama Lengkap')
    no_handphone = forms.CharField(max_length=15, label='No Handphone')
    bidang = forms.ChoiceField(choices=SUBJECT_CHOICES,
                               help_text="Bidang hanya dapat diatur sekali di awal.")
    role = forms.ChoiceField(choices=ROLE_CHOICES,
                             help_text="Role hanya dapat diatur sekali di awal. Nilai guru tidak disertakan dalam ranking.")

    asal_sekolah = forms.CharField(max_length=100, label='Asal Sekolah')
    kota = forms.CharField(max_length=100)
    provinsi = forms.CharField(max_length=100)

    # data opsional
    guru_pembimbing = forms.CharField(max_length=100,
                                      required=False,
                                      help_text="Opsional",
                                      label='Guru Pembimbing')
    no_handphone_guru = forms.CharField(max_length=15,
                                        required=False,
                                        help_text="Opsional",
                                        label='No Handphone Guru')

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = UserProfile(user=user,
                                   nama_lengkap=self.cleaned_data['nama_lengkap'],
                                   no_handphone=self.cleaned_data['no_handphone'],
                                   bidang=self.cleaned_data['bidang'],
                                   role=self.cleaned_data['role'],
                                   asal_sekolah=self.cleaned_data['asal_sekolah'],
                                   kota=self.cleaned_data['kota'],
                                   provinsi=self.cleaned_data['provinsi'],
                                   guru_pembimbing=self.cleaned_data['guru_pembimbing'],
                                   no_handphone_guru=self.cleaned_data['no_handphone_guru'])
        user_profile.save()
        return user, user_profile
