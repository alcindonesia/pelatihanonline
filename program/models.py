from django.db import models
from django.utils import timezone
from soal.models import BundelSoal


class Program(models.Model):
    nama_program = models.CharField(max_length=100)
    deskripsi = models.TextField(default="-")

    def __str__(self):
        return self.nama_program

    def event_count(self):
        return self.event_set.count()

    event_count.short_description = 'Jumlah Event'



class Event(models.Model):
    nama_event = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    jadwal = models.CharField(max_length=100, default="-")
    aktif = models.BooleanField(default=True)
    link_panduan = models.URLField(blank=True, null=True)
    waktu_buka = models.DateTimeField(blank=True, null=True)
    waktu_mulai = models.DateTimeField(blank=True, null=True)
    waktu_selesai = models.DateTimeField(blank=True, null=True)
    waktu_download = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.nama_event

    def paket_count(self):
        return self.paket_set.count()

    paket_count.short_description = 'Jumlah Paket'

    def status(self):
        now = timezone.now()
        try:
            if (now > self.waktu_selesai):
                return "Program Selesai"
            elif (now > self.waktu_mulai):
                return "Program Berjalan"
            elif (now > self.waktu_buka):
                return "Pendaftaran Dibuka"
            else:
                return "Segera Hadir"
        except:
            return "Segera Hadir"

    status.short_description = 'Status'

    def mulai(self):
        now = timezone.now()
        return (now > self.waktu_mulai)

    def selesai(self):
        now = timezone.now()
        return (now > self.waktu_selesai)

    def buka(self):
        now = timezone.now()
        return (now > self.waktu_buka)

    def download(self):
        now = timezone.now()
        return (now > self.waktu_download)


class NomorPaket(models.Model):
    kode = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.kode



class Paket(models.Model):
    nama_paket = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    nomor_paket = models.ForeignKey(NomorPaket, on_delete=models.CASCADE)
    bundel_soal = models.ForeignKey(BundelSoal, on_delete=models.CASCADE)
    open_time = models.DateTimeField('Open Time')
    close_time = models.DateTimeField('Close Time')

    def __str__(self):
        return self.nama_paket

    def open_time_format(self):
        return self.open_time.strftime("%A, %d-%m-%Y %H:%M")

    open_time_format.short_description = 'Open Time'

    def close_time_format(self):
        return self.close_time.strftime("%A, %d-%m-%Y %H:%M")

    close_time_format.short_description = 'Close Time'

    def mulai(self):
        now = timezone.now()
        return (now > self.open_time)

    def selesai(self):
        now = timezone.now()
        return (now > self.close_time)
