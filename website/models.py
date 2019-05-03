from django.db import models


class Testimoni(models.Model):
    nama = models.CharField(max_length=100)
    teks = models.TextField(default='-')
    foto = models.ImageField(upload_to='photo/')

class Pengumuman(models.Model):
    judul = models.CharField(max_length=100)
    teks = models.TextField(default='-')
