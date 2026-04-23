from django.db import models
from django.contrib.auth.models import User

class Haber(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField(blank=True)
    resim = models.ImageField(upload_to='haberler/', blank=True, null=True)
    renk = models.CharField(max_length=20, default='#1a3a5c')
    etiket = models.CharField(max_length=50, default='DUYURU')
    tarih = models.DateTimeField(auto_now_add=True)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.baslik

    def delete(self, *args, **kwargs):
        if self.resim:
            self.resim.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['-tarih']

class Ilan(models.Model):
    ISITMA_SECENEKLERI = [
        ('dogalgaz', 'Doğalgaz'),
        ('kombi', 'Kombi'),
        ('merkezi', 'Merkezi'),
        ('klima', 'Klima'),
        ('soba', 'Soba'),
    ]
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField(blank=True)
    konum = models.CharField(max_length=200)
    oda_sayisi = models.CharField(max_length=10, default='1+1')
    kat = models.IntegerField(default=0)
    metrekare = models.IntegerField(default=0)
    bina_yasi = models.IntegerField(default=0)
    banyo = models.IntegerField(default=1)
    balkon = models.BooleanField(default=False)
    asansor = models.BooleanField(default=False)
    site_icinde = models.BooleanField(default=False)
    site_aidati = models.IntegerField(default=0)
    isitma = models.CharField(max_length=20, choices=ISITMA_SECENEKLERI, default='dogalgaz')
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik

    def delete(self, *args, **kwargs):
        for medya in self.medyalar.all():
            medya.delete()
        super().delete(*args, **kwargs)

class IlanMedya(models.Model):
    MEDYA_TIPLERI = [
        ('resim', 'Resim'),
        ('video', 'Video'),
    ]
    ilan = models.ForeignKey(Ilan, on_delete=models.CASCADE, related_name='medyalar')
    dosya = models.ImageField(upload_to='medya/')
    tip = models.CharField(max_length=10, choices=MEDYA_TIPLERI, default='resim')

    def delete(self, *args, **kwargs):
        if self.dosya:
            self.dosya.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.ilan.baslik} - {self.tip}"

class Favori(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    ilan = models.ForeignKey(Ilan, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('kullanici', 'ilan')

    def __str__(self):
        return f"{self.kullanici} - {self.ilan.baslik}"
class Hutbe(models.Model):
    baslik = models.CharField(max_length=200)
    tarih = models.DateField()
    normal_pdf = models.FileField(upload_to='hutbeler/')
    telefon_pdf = models.FileField(upload_to='hutbeler/')
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.baslik

    class Meta:
        ordering = ['-tarih']

class Hutbe(models.Model):
    baslik = models.CharField(max_length=200)
    tarih = models.DateField()
    normal_pdf = models.FileField(upload_to='hutbeler/')
    telefon_pdf = models.FileField(upload_to='hutbeler/')
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.baslik

    class Meta:
        ordering = ['-tarih']
