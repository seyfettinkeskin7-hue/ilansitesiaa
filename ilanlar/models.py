from storages.backends.gcloud import GoogleCloudStorage

class InlinePDFStorage(GoogleCloudStorage):
    def url(self, name):
        url = super().url(name)
        return url

    def _save(self, name, content):
        from google.cloud.storage import Blob
        self.object_parameters = {'content_disposition': 'inline'}
        return super()._save(name, content)

from django.db import models
from django.contrib.auth.models import User

class Haber(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField(blank=True)  # kısa özet
    icerik = models.TextField(blank=True)  # uzun yazı
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
    aciklama = models.TextField(blank=True)  # kısa özet
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
    normal_pdf = models.FileField(upload_to='hutbeler/', storage=InlinePDFStorage())
    telefon_pdf = models.FileField(upload_to='hutbeler/', storage=InlinePDFStorage())
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.baslik

    class Meta:
        ordering = ['-tarih']

class Hutbe(models.Model):
    baslik = models.CharField(max_length=200)
    tarih = models.DateField()
    normal_pdf = models.FileField(upload_to='hutbeler/', storage=InlinePDFStorage())
    telefon_pdf = models.FileField(upload_to='hutbeler/', storage=InlinePDFStorage())
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.baslik

    class Meta:
        ordering = ['-tarih']

class AkademiKategori(models.Model):
    ad = models.CharField(max_length=200)
    sira = models.IntegerField(default=0)

    def __str__(self):
        return self.ad

    class Meta:
        ordering = ['sira']
        verbose_name = 'Akademi Kategorisi'
        verbose_name_plural = 'Akademi Kategorileri'

class Akademi(models.Model):
    kategori = models.ForeignKey(AkademiKategori, on_delete=models.CASCADE, related_name='akademiler')
    ad = models.CharField(max_length=200)
    sehir = models.CharField(max_length=100, blank=True)
    aciklama = models.TextField(blank=True)
    resmi_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    konum_url = models.URLField(blank=True, help_text='Google Maps adres linki')
    sira = models.IntegerField(default=0)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.ad

    class Meta:
        ordering = ['sira']
        verbose_name = 'Akademi'
        verbose_name_plural = 'Akademiler'

class AkademiResim(models.Model):
    akademi = models.ForeignKey(Akademi, on_delete=models.CASCADE, related_name='resimler')
    resim = models.ImageField(upload_to='akademi/')
    sira = models.IntegerField(default=0)

    def delete(self, *args, **kwargs):
        if self.resim:
            self.resim.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['sira']
        verbose_name = 'Akademi Resmi'
        verbose_name_plural = 'Akademi Resimleri'

class AkademiGorevli(models.Model):
    UNVAN_SECENEKLERI = [
        ('mudur', 'Merkez Müdürü'),
        ('mudur_yardimcisi', 'Müdür Yardımcısı'),
        ('egitim_gorevlisi', 'Eğitim Görevlisi'),
    ]
    akademi = models.ForeignKey(Akademi, on_delete=models.CASCADE, related_name='gorevliler')
    ad = models.CharField(max_length=200)
    unvan = models.CharField(max_length=30, choices=UNVAN_SECENEKLERI, default='egitim_gorevlisi')
    foto = models.ImageField(upload_to='gorevliler/', blank=True, null=True)
    biyografi = models.TextField(blank=True)
    egitim = models.TextField(blank=True, help_text='Her satıra bir eğitim bilgisi yaz')
    uzmanlik = models.CharField(max_length=300, blank=True, help_text='Virgülle ayır: Tecvid, Kıraat, Hadis')
    deneyim_yil = models.IntegerField(default=0)
    mezun_ogrenci = models.IntegerField(default=0)
    sira = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ad} - {self.get_unvan_display()}"

    def delete(self, *args, **kwargs):
        if self.foto:
            self.foto.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['sira']
        verbose_name = 'Akademi Görevlisi'
        verbose_name_plural = 'Akademi Görevlileri'

class Bildirim(models.Model):
    baslik = models.CharField(max_length=200, blank=True)
    mesaj = models.TextField()
    aktif = models.BooleanField(default=True)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik or self.mesaj[:50]

    class Meta:
        ordering = ['-tarih']
        verbose_name = 'Bildirim'
        verbose_name_plural = 'Bildirimler'
