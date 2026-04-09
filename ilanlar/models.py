from django.db import models
from django.contrib.auth.models import User

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

class IlanMedya(models.Model):
    MEDYA_TIPLERI = [
        ('resim', 'Resim'),
        ('video', 'Video'),
    ]
    ilan = models.ForeignKey(Ilan, on_delete=models.CASCADE, related_name='medyalar')
    dosya = models.FileField(upload_to='medya/')
    tip = models.CharField(max_length=10, choices=MEDYA_TIPLERI, default='resim')

    def __str__(self):
        return f"{self.ilan.baslik} - {self.tip}"

class Favori(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    ilan = models.ForeignKey(Ilan, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('kullanici', 'ilan')

    def __str__(self):
        return f"{self.kullanici} - {self.ilan.baslik}"