from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Ilan, IlanMedya, Favori

def anasayfa(request):
    if not request.user.is_authenticated:
        return redirect('/giris/')
    
    arama = request.GET.get('arama', '').strip()
    
    if arama:
        ilanlar = Ilan.objects.filter(
            Q(konum__icontains=arama) |
            Q(baslik__icontains=arama)
        ).order_by('-tarih')
    else:
        ilanlar = Ilan.objects.all().order_by('-tarih')
    
    favori_idler = Favori.objects.filter(kullanici=request.user).values_list('ilan_id', flat=True)
    favoriler = Ilan.objects.filter(id__in=favori_idler)
    return render(request, 'anasayfa.html', {
        'ilanlar': ilanlar,
        'favori_idler': list(favori_idler),
        'favoriler': favoriler,
        'arama': arama,
    })

def detay(request, ilan_id):
    if not request.user.is_authenticated:
        return redirect('/giris/')
    ilan = get_object_or_404(Ilan, id=ilan_id)
    favori = Favori.objects.filter(kullanici=request.user, ilan=ilan).exists()
    return render(request, 'detay.html', {'ilan': ilan, 'favori': favori})

def kayit(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'kayit.html', {'form': form})

@csrf_exempt
def giris(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'giris.html', {'form': form})

def cikis(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/giris/')

def ilan_ekle(request):
    if not request.user.is_authenticated:
        return redirect('/giris/')
    if request.method == 'POST':
        ilan = Ilan.objects.create(
            baslik=request.POST.get('baslik', ''),
            aciklama=request.POST.get('aciklama', ''),
            konum=request.POST.get('konum', ''),
            oda_sayisi=request.POST.get('oda_sayisi', '1+1'),
            kat=int(request.POST.get('kat') or 0),
            metrekare=int(request.POST.get('metrekare') or 0),
            bina_yasi=int(request.POST.get('bina_yasi') or 0),
            banyo=int(request.POST.get('banyo') or 1),
            isitma=request.POST.get('isitma', 'dogalgaz'),
            balkon='balkon' in request.POST,
            asansor='asansor' in request.POST,
            site_icinde='site_icinde' in request.POST,
            site_aidati=int(request.POST.get('site_aidati') or 0),
            kullanici=request.user,
        )
        for resim in request.FILES.getlist('resimler'):
            IlanMedya.objects.create(ilan=ilan, dosya=resim, tip='resim')
        for video in request.FILES.getlist('videolar'):
            IlanMedya.objects.create(ilan=ilan, dosya=video, tip='video')
        return redirect('/')
    return render(request, 'ilan_ekle.html')

def ilan_sil(request, ilan_id):
    ilan = get_object_or_404(Ilan, id=ilan_id, kullanici=request.user)
    if request.method == 'POST':
        ilan.delete()
    return redirect('/')

def favori_ekle(request, ilan_id):
    if not request.user.is_authenticated:
        return redirect('/giris/')
    ilan = get_object_or_404(Ilan, id=ilan_id)
    favori, olusturuldu = Favori.objects.get_or_create(kullanici=request.user, ilan=ilan)
    if not olusturuldu:
        favori.delete()
    return redirect(request.META.get('HTTP_REFERER', '/')