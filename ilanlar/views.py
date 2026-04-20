from django.shortcuts import render, redirect
from .models import Haber, Ilan, Favori

MUFTULUK_VERISI = {
    # ... (aynı kalıyor, değiştirme)
}

def animasyon(request):
    return render(request, 'animasyon.html')

def anasayfa(request):
    haberler = Haber.objects.filter(aktif=True).order_by('-tarih')
    return render(request, 'anasayfa.html', {'haberler': haberler})

def muftulukler(request):
    iller = sorted(MUFTULUK_VERISI.keys())
    return render(request, 'muftulukler.html', {'iller': iller})

def muftuluk_il(request, il):
    bulunan_il = None
    for key in MUFTULUK_VERISI.keys():
        slug = key.lower().replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')
        if slug == il.lower():
            bulunan_il = key
            break
    if bulunan_il:
        ilceler = MUFTULUK_VERISI[bulunan_il]
    else:
        ilceler = []
    return render(request, 'muftuluk_il.html', {'il': bulunan_il or il, 'ilceler': ilceler})

def detay(request, ilan_id): return render(request, 'detay.html')
def kayit(request): return render(request, 'kayit.html')
def giris(request): return render(request, 'giris.html')
def cikis(request): return render(request, 'anasayfa.html')
def ilan_ekle(request): return render(request, 'ilan_ekle.html')
def ilan_sil(request, ilan_id): return render(request, 'panel.html')
def favori_ekle(request, ilan_id): return render(request, 'anasayfa.html')
def panel(request): return render(request, 'panel.html')
def haber_ekle(request): return render(request, 'panel.html')
def haber_sil(request, haber_id): return render(request, 'panel.html')
def akademi(request): return render(request, 'akademi.html')