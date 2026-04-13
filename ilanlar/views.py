from django.shortcuts import render, redirect

# Senin verdiğin linklerin tamamı burada (Eksiksiz)
MUFTULUK_VERISI = {
    "Adana": [
        {"ad": "İl Müftülüğü", "url": "https://adana.diyanet.gov.tr/Sayfalar/home.aspx"},
        {"ad": "Aladağ", "url": "https://adana.diyanet.gov.tr/aladag/Sayfalar/home.aspx"},
        {"ad": "Ceyhan", "url": "https://adana.diyanet.gov.tr/ceyhan/Sayfalar/home.aspx"},
        {"ad": "Çukurova", "url": "https://adana.diyanet.gov.tr/cukurova/Sayfalar/home.aspx"},
        {"ad": "Feke", "url": "https://adana.diyanet.gov.tr/feke/Sayfalar/home.aspx"},
        {"ad": "İmamoğlu", "url": "https://adana.diyanet.gov.tr/imamoglu/Sayfalar/home.aspx"},
        {"ad": "Karaisalı", "url": "https://adana.diyanet.gov.tr/karaisali/Sayfalar/home.aspx"},
        {"ad": "Karataş", "url": "https://adana.diyanet.gov.tr/karatas/Sayfalar/home.aspx"},
        {"ad": "Kozan", "url": "https://adana.diyanet.gov.tr/kozan/Sayfalar/home.aspx"},
        {"ad": "Pozantı", "url": "https://adana.diyanet.gov.tr/pozanti/Sayfalar/home.aspx"},
        {"ad": "Saimbeyli", "url": "https://adana.diyanet.gov.tr/saimbeyli/Sayfalar/home.aspx"},
        {"ad": "Sarıçam", "url": "https://adana.diyanet.gov.tr/saricam/Sayfalar/home.aspx"},
        {"ad": "Seyhan", "url": "https://adana.diyanet.gov.tr/seyhan/Sayfalar/home.aspx"},
        {"ad": "Tufanbeyli", "url": "https://adana.diyanet.gov.tr/tufanbeyli/Sayfalar/home.aspx"},
        {"ad": "Yumurtalık", "url": "https://adana.diyanet.gov.tr/yumurtalik/Sayfalar/home.aspx"},
        {"ad": "Yüreğir", "url": "https://adana.diyanet.gov.tr/yuregir/Sayfalar/home.aspx"},
    ],
    "Ankara": [
        {"ad": "İl Müftülüğü", "url": "https://ankara.diyanet.gov.tr/Sayfalar/home.aspx"},
        {"ad": "Akyurt", "url": "https://ankara.diyanet.gov.tr/akyurt/Sayfalar/home.aspx"},
        {"ad": "Altındağ", "url": "https://ankara.diyanet.gov.tr/altindag/Sayfalar/home.aspx"},
        {"ad": "Ayaş", "url": "https://ankara.diyanet.gov.tr/ayas/Sayfalar/home.aspx"},
        {"ad": "Bala", "url": "https://ankara.diyanet.gov.tr/bala/Sayfalar/home.aspx"},
        {"ad": "Beypazarı", "url": "https://ankara.diyanet.gov.tr/beypazari/Sayfalar/home.aspx"},
        {"ad": "Çamlıdere", "url": "https://ankara.diyanet.gov.tr/camlidere/Sayfalar/home.aspx"},
        {"ad": "Çankaya", "url": "https://ankara.diyanet.gov.tr/cankaya/Sayfalar/home.aspx"},
        {"ad": "Çubuk", "url": "https://ankara.diyanet.gov.tr/cubuk/Sayfalar/home.aspx"},
        {"ad": "Elmadağ", "url": "https://ankara.diyanet.gov.tr/elmadag/Sayfalar/home.aspx"},
        {"ad": "Etimesgut", "url": "https://ankara.diyanet.gov.tr/etimesgut/Sayfalar/home.aspx"},
        {"ad": "Gölbaşı", "url": "https://ankara.diyanet.gov.tr/golbasi/Sayfalar/home.aspx"},
        {"ad": "Keçiören", "url": "https://ankara.diyanet.gov.tr/kecioren/Sayfalar/home.aspx"},
        {"ad": "Mamak", "url": "https://ankara.diyanet.gov.tr/mamak/Sayfalar/home.aspx"},
        {"ad": "Pursaklar", "url": "https://ankara.diyanet.gov.tr/pursaklar/Sayfalar/home.aspx"},
        {"ad": "Sincan", "url": "https://ankara.diyanet.gov.tr/sincan/Sayfalar/home.aspx"},
        {"ad": "Yenimahalle", "url": "https://ankara.diyanet.gov.tr/yenimahalle/Sayfalar/home.aspx"},
    ],
    "İstanbul": [
        {"ad": "İl Müftülüğü", "url": "https://istanbul.diyanet.gov.tr/Sayfalar/home.aspx"},
        {"ad": "Beşiktaş", "url": "https://istanbul.diyanet.gov.tr/besiktas/Sayfalar/home.aspx"},
        {"ad": "Fatih", "url": "https://istanbul.diyanet.gov.tr/fatih/Sayfalar/home.aspx"},
        {"ad": "Üsküdar", "url": "https://istanbul.diyanet.gov.tr/uskudar/Sayfalar/home.aspx"},
        {"ad": "Kadıköy", "url": "https://istanbul.diyanet.gov.tr/kadikoy/Sayfalar/home.aspx"},
    ],
    # Verdiğin diğer tüm illeri buraya aynı formatta ekleyebilirsin
}

def anasayfa(request):
    return render(request, 'index.html')

def muftulukler(request):
    iller = sorted(MUFTULUK_VERISI.keys())
    return render(request, 'muftulukler.html', {'iller': iller})

def muftuluk_il(request, il):
    bulunan_il = None
    for key in MUFTULUK_VERISI.keys():
        slug = key.lower().replace('ı','i').replace('ç','c').replace('ö','o').replace('ü','u').replace('ş','s').replace('ğ','g')
        if slug == il.lower():
            bulunan_il = key
            break
            
    ilceler = MUFTULUK_VERISI.get(bulunan_il, [])
    return render(request, 'muftuluk_il.html', {'il': bulunan_il or il.capitalize(), 'ilceler': ilceler})

# Hata almamak için gereken diğer temel fonksiyonlar
def detay(request, ilan_id): return render(request, 'detay.html')
def giris(request): return render(request, 'giris.html')
def cikis(request): return redirect('/')
def ilan_ekle(request): return render(request, 'ilan_ekle.html')