from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Haber, Ilan, IlanMedya, Favori

MUFTULUK_VERISI = {
    # ... (aynı kalıyor, değiştirme)
}

def animasyon(request):
    return render(request, 'animasyon.html')

def anasayfa(request):
    haberler = Haber.objects.filter(aktif=True).order_by('-tarih')
    ilanlar = Ilan.objects.all().order_by('-tarih')
    return render(request, 'anasayfa.html', {'haberler': haberler, 'ilanlar': ilanlar})

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
    ilceler = MUFTULUK_VERISI[bulunan_il] if bulunan_il else []
    return render(request, 'muftuluk_il.html', {'il': bulunan_il or il, 'ilceler': ilceler})

def kayit(request):
    if request.method == 'POST':
        kullanici_adi = request.POST.get('kullanici_adi')
        email = request.POST.get('email')
        sifre = request.POST.get('sifre')
        sifre2 = request.POST.get('sifre2')
        if sifre != sifre2:
            messages.error(request, 'Şifreler eşleşmiyor!')
            return render(request, 'kayit.html')
        if User.objects.filter(username=kullanici_adi).exists():
            messages.error(request, 'Bu kullanıcı adı zaten alınmış!')
            return render(request, 'kayit.html')
        user = User.objects.create_user(username=kullanici_adi, email=email, password=sifre)
        login(request, user)
        return redirect('anasayfa')
    return render(request, 'kayit.html')

def giris(request):
    if request.method == 'POST':
        kullanici_adi = request.POST.get('kullanici_adi')
        sifre = request.POST.get('sifre')
        user = authenticate(request, username=kullanici_adi, password=sifre)
        if user:
            login(request, user)
            return redirect('anasayfa')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı!')
    return render(request, 'giris.html')

def cikis(request):
    logout(request)
    return redirect('anasayfa')

def ilan_ekle(request):
    if not request.user.is_authenticated:
        return redirect('giris')
    if request.method == 'POST':
        ilan = Ilan.objects.create(
            kullanici=request.user,
            baslik=request.POST.get('baslik'),
            aciklama=request.POST.get('aciklama'),
            konum=request.POST.get('konum'),
            oda_sayisi=request.POST.get('oda_sayisi', '1+1'),
            kat=request.POST.get('kat', 0),
            metrekare=request.POST.get('metrekare', 0),
            bina_yasi=request.POST.get('bina_yasi', 0),
            banyo=request.POST.get('banyo', 1),
            balkon='balkon' in request.POST,
            asansor='asansor' in request.POST,
            site_icinde='site_icinde' in request.POST,
            site_aidati=request.POST.get('site_aidati', 0),
            isitma=request.POST.get('isitma', 'dogalgaz'),
        )
        for dosya in request.FILES.getlist('resimler'):
            IlanMedya.objects.create(ilan=ilan, dosya=dosya, tip='resim')
        return redirect('anasayfa')
    return render(request, 'ilan_ekle.html')

def ilan_sil(request, ilan_id):
    if not request.user.is_authenticated:
        return redirect('giris')
    ilan = get_object_or_404(Ilan, id=ilan_id, kullanici=request.user)
    ilan.delete()
    return redirect('panel')

def detay(request, ilan_id):
    ilan = get_object_or_404(Ilan, id=ilan_id)
    return render(request, 'detay.html', {'ilan': ilan})

def favori_ekle(request, ilan_id):
    if not request.user.is_authenticated:
        return redirect('giris')
    ilan = get_object_or_404(Ilan, id=ilan_id)
    favori, created = Favori.objects.get_or_create(kullanici=request.user, ilan=ilan)
    if not created:
        favori.delete()
    return redirect('anasayfa')

def panel(request):
    if not request.user.is_authenticated:
        return redirect('giris')
    ilanlar = Ilan.objects.filter(kullanici=request.user)
    return render(request, 'panel.html', {'ilanlar': ilanlar})

def haber_ekle(request):
    return redirect('panel')

def haber_sil(request, haber_id):
    return redirect('panel')

def akademi(request):
    return render(request, 'akademi.html')
