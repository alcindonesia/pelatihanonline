import random, string
from django.db import models
from django.forms.models import model_to_dict
from pelatihanonline.constants import SUBJECT_CHOICES, ANSWER_CHOICES

class BundelSoal(models.Model):
    nama_bundel_soal = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_bundel_soal

    def soal_count(self):
        return self.soal_set.count()

    soal_count.short_description = 'Jumlah Soal'


def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def file_path(instance, filename):
    name, ext = filename.split('.')
    return '{}/{}_{}.{}'.format('pdf', name, randomword(6), ext)


class Soal(models.Model):
    nama_soal = models.CharField(max_length=100)
    bundel_soal = models.ForeignKey(BundelSoal, on_delete=models.CASCADE)
    bidang = models.CharField(max_length=3, choices=SUBJECT_CHOICES)
    judul_materi = models.CharField(max_length=100, default="")
    file_soal = models.FileField(upload_to=file_path)
    file_solusi = models.FileField(upload_to=file_path)
    no1 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no2 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no3 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no4 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no5 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no6 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no7 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no8 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no9 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no10 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no11 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no12 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no13 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no14 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no15 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no16 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no17 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no18 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no19 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no20 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no21 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no22 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no23 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no24 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no25 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no26 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no27 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no28 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no29 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no30 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')

    def __str__(self):
        return self.nama_soal


class Submission(models.Model):
    userprofile = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE)
    bidang = models.CharField(max_length=3, choices=SUBJECT_CHOICES)
    paket = models.ForeignKey('program.Paket', on_delete=models.CASCADE)
    graded = models.BooleanField('Sudah Dinilai?', default=False)
    nilai = models.IntegerField(default=0)
    no1 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no2 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no3 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no4 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no5 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no6 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no7 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no8 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no9 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no10 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no11 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no12 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no13 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no14 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no15 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no16 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no17 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no18 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no19 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no20 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no21 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no22 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no23 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no24 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no25 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no26 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no27 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no28 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no29 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no30 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')

    def __str__(self):
        nama_lengkap_user = self.userprofile.nama_lengkap
        jawaban = "".join([str(self.no1),str(self.no2),str(self.no3),str(self.no4),str(self.no5),str(self.no6),str(self.no7),str(self.no8),str(self.no9),str(self.no10),
                           str(self.no1),str(self.no12),str(self.no13),str(self.no14),str(self.no15),str(self.no16),str(self.no17),str(self.no18),str(self.no19),str(self.no20),
                           str(self.no1),str(self.no22),str(self.no23),str(self.no24),str(self.no25),str(self.no26),str(self.no27),str(self.no28),str(self.no29),str(self.no30)])
        return " - ".join([self.userprofile.user.username,
                           nama_lengkap_user, self.bidang,
                           self.paket.nama_paket,
                           jawaban])

    def grade(self):
        nilai = 0
        jumlah_soal = 0
        soal = self.paket.bundel_soal.soal_set.get(bidang=self.bidang)
        soal_dict = model_to_dict(soal)
        sub_dict = model_to_dict(self)
        for i in range(1, 31):
            if soal_dict['no' + str(i)] != '-':
                jumlah_soal = jumlah_soal + 1
                if sub_dict['no' + str(i)] == soal_dict['no' + str(i)]:
                    nilai = nilai + 1

        self.nilai = (nilai * 100) // jumlah_soal
        self.graded = True
        self.save()
        return self.nilai
