import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ilanSitesi.settings')
django.setup()

from django.contrib.auth.models import User
from ilanlar.models import Ilan

admin = User.objects.filter(is_superuser=True).first()

camiler = [
    {"baslik": "ACISU YAYLASI ŞİFA CAMİİ Lojmanı", "konum": "Adana / Aladağ", "lojman": True},
    {"baslik": "BİŞR-İ HAFİ CAMİİ Lojmanı", "konum": "Adana / Aladağ", "lojman": False},
    {"baslik": "ÇAKIRLAR MH. CAMİİ Lojmanı", "konum": "Adana / Aladağ", "lojman": True},
    {"baslik": "ÇÖMEKLİ MH. CAMİİ Lojmanı", "konum": "Adana / Aladağ", "lojman": True},
    {"baslik": "DAİLER MH. CAMİİ Lojmanı", "konum": "Adana / Aladağ", "lojman": True},
    {"baslik": "DARIÇUKURU MH. CAMİİ Lojmanı", "konum": "Adana / Aladağ", "lojman": True},
    {"baslik": "EBRİŞİM MH. TEKİR CAMİİ Lojmanı", "konum": "Adana / Aladağ", "lojman": True},
    {"baslik": "KAYABAŞI MH. CAMİİ Lojmanı", "konum": "Adana / Aladağ", "lojman": True},
    {"baslik": "EYYUBİYE CAMİİ Lojmanı", "konum": "Adana / Ceyhan", "lojman": True},
    {"baslik": "YEŞİLLER CAMİİ Lojmanı", "konum": "Adana / Ceyhan", "lojman": True},
    {"baslik": "BAHÇELİEVLER CAMİİ Lojmanı", "konum": "Adana / Ceyhan", "lojman": True},
    {"baslik": "RAMAZANOĞLU CAMİİ Lojmanı", "konum": "Adana / Çukurova", "lojman": True},
    {"baslik": "HOŞKADEM CAMİİ Lojmanı", "konum": "Adana / Kozan", "lojman": True},
    {"baslik": "HALİLURRAHMAN CAMİİ Lojmanı", "konum": "Adana / Yüreğir", "lojman": True},
    {"baslik": "HARRAN CAMİİ Lojmanı", "konum": "Adana / Yüreğir", "lojman": True},
    {"baslik": "ANADOLU CAMİİ Lojmanı", "konum": "Adana / Yüreğir", "lojman": True},
    {"baslik": "ESADİYE CAMİİ Lojmanı", "konum": "Adana / Yüreğir", "lojman": True},
]

eklenen = 0
for cami in camiler:
    if not Ilan.objects.filter(baslik=cami["baslik"]).exists():
        Ilan.objects.create(
            kullanici=admin,
            baslik=cami["baslik"],
            aciklama=f"Diyanet İşleri Başkanlığı münhal lojman ilanı. {'Lojmanı Var' if cami['lojman'] else 'Lojmanı Yok'}",
            konum=cami["konum"],
            onaylandi=True,
        )
        eklenen += 1

print(f"{eklenen} cami lojmanı eklendi!")
