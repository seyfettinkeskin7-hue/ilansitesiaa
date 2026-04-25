from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Haber, Ilan, IlanMedya, Favori

MUFTULUK_VERISI = {
    # ... (aynı kalıyor, değiştirme)
}

def animasyon(request):
    if request.COOKIES.get("animasyon_goruldu"):
        return redirect("anasayfa")
    return render(request, 'animasyon.html')

def anasayfa(request):
    if not request.user.is_authenticated:
        return redirect('giris')
    from .models import Bildirim
    haberler = Haber.objects.filter(aktif=True).order_by('-tarih')
    ilanlar = Ilan.objects.all().order_by('-tarih')[:30]
    ilanlar2 = Ilan.objects.all().order_by('?')[:30]
    favori_idler = list(Favori.objects.filter(kullanici=request.user).values_list('ilan_id', flat=True))
    favoriler = Favori.objects.filter(kullanici=request.user).select_related('ilan')
    bildirim = Bildirim.objects.filter(aktif=True).first()
    return render(request, 'anasayfa.html', {'haberler': haberler, 'ilanlar': ilanlar, 'ilanlar2': ilanlar2, 'favori_idler': favori_idler, 'favoriler': favoriler, 'bildirim': bildirim})

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
        kullanici_adi = request.POST.get('username')
        email = request.POST.get('email')
        sifre = request.POST.get('password')
        sifre2 = request.POST.get('sifre2')
        if sifre != sifre2:
            messages.error(request, 'Şifreler eşleşmiyor!')
            return render(request, 'kayit.html')
        if User.objects.filter(username=kullanici_adi).exists():
            messages.error(request, 'Bu kullanıcı adı zaten alınmış!')
            return render(request, 'kayit.html')
        user = User.objects.create_user(username=kullanici_adi, email=email, password=sifre)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        from django.contrib import messages
        messages.success(request, 'İlanınız alındı! Kontrol yapıldıktan sonra yayına alınacaktır.')
        return redirect('anasayfa')
    return render(request, 'kayit.html')

def giris(request):
    if request.method == 'POST':
        kullanici_adi = request.POST.get('username')
        sifre = request.POST.get('password')
        user = authenticate(request, username=kullanici_adi, password=sifre)
        if user:
            login(request, user)
            from django.contrib import messages
        messages.success(request, 'İlanınız alındı! Kontrol yapıldıktan sonra yayına alınacaktır.')
        return redirect('anasayfa')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı!')
    return render(request, 'giris.html')

def cikis(request):
    logout(request)
    return redirect('giris')

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
            kat=int(request.POST.get('kat') or 0),
            metrekare=int(request.POST.get('metrekare') or 0),
            bina_yasi=int(request.POST.get('bina_yasi') or 0),
            banyo=int(request.POST.get('banyo') or 1),
            balkon='balkon' in request.POST,
            asansor='asansor' in request.POST,
            site_icinde='site_icinde' in request.POST,
            site_aidati=int(request.POST.get('site_aidati') or 0),
            isitma=request.POST.get('isitma', 'dogalgaz'),
        )
        for dosya in request.FILES.getlist('resimler'):
            IlanMedya.objects.create(ilan=ilan, dosya=dosya, tip='resim')
        from django.contrib import messages
        messages.success(request, 'İlanınız alındı! Kontrol yapıldıktan sonra yayına alınacaktır.')
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
    favori = False
    if request.user.is_authenticated:
        favori = Favori.objects.filter(kullanici=request.user, ilan=ilan).exists()
    return render(request, 'detay.html', {'ilan': ilan, 'favori': favori})

def favori_ekle(request, ilan_id):
    if not request.user.is_authenticated:
        return redirect('giris')
    ilan = get_object_or_404(Ilan, id=ilan_id)
    favori, created = Favori.objects.get_or_create(kullanici=request.user, ilan=ilan)
    if not created:
        favori.delete()
    next_url = request.META.get('HTTP_REFERER', '/')
    return redirect(next_url)

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
    from .models import AkademiKategori
    kategoriler = AkademiKategori.objects.prefetch_related('akademiler').all()
    return render(request, 'akademi.html', {'kategoriler': kategoriler})

def favorilerim(request):
    if not request.user.is_authenticated:
        return redirect('giris')
    favoriler = Favori.objects.filter(kullanici=request.user).select_related('ilan')
    return render(request, 'favorilerim.html', {'favoriler': favoriler})

def hutbeler(request):
    if not request.user.is_authenticated:
        return redirect('giris')
    from .models import Hutbe
    hutbeler = Hutbe.objects.filter(aktif=True)
    return render(request, 'hutbeler.html', {'hutbeler': hutbeler})

def tum_ilanlar(request):
    if not request.user.is_authenticated:
        return redirect('giris')
    arama = request.GET.get('arama', '')
    ilanlar = Ilan.objects.all().order_by('-tarih')
    if arama:
        ilanlar = ilanlar.filter(konum__icontains=arama) | ilanlar.filter(baslik__icontains=arama)
    return render(request, 'ilanlar.html', {'ilanlar': ilanlar, 'arama': arama})


def haber_detay(request, haber_id):
    from .models import Haber
    haber = Haber.objects.get(id=haber_id, aktif=True)
    return render(request, "haber_detay.html", {"haber": haber})

def akademi_detay(request, akademi_id):
    from .models import Akademi
    akademi = get_object_or_404(Akademi, id=akademi_id, aktif=True)
    return render(request, 'akademi_detay.html', {'akademi': akademi})

def gorevli_detay(request, gorevli_id):
    from .models import AkademiGorevli
    gorevli = get_object_or_404(AkademiGorevli, id=gorevli_id)
    return render(request, 'gorevli_detay.html', {'gorevli': gorevli})
