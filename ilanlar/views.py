from django.shortcuts import render

# Paylaştığın tüm linklerin listesi
MUFTULUK_VERISI = {
    "Adana": [
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
    "Adıyaman": [
        {"ad": "Besni", "url": "https://adiyaman.diyanet.gov.tr/besni/Sayfalar/home.aspx"},
        {"ad": "Çelikhan", "url": "https://adiyaman.diyanet.gov.tr/celikhan/Sayfalar/home.aspx"},
        {"ad": "Gerger", "url": "https://adiyaman.diyanet.gov.tr/gerger/Sayfalar/home.aspx"},
        {"ad": "Gölbaşı", "url": "https://adiyaman.diyanet.gov.tr/golbasi/Sayfalar/home.aspx"},
        {"ad": "Kahta", "url": "https://adiyaman.diyanet.gov.tr/kahta/Sayfalar/home.aspx"},
        {"ad": "Samsat", "url": "https://adiyaman.diyanet.gov.tr/samsat/Sayfalar/home.aspx"},
        {"ad": "Sincik", "url": "https://adiyaman.diyanet.gov.tr/sincik/Sayfalar/home.aspx"},
        {"ad": "Tut", "url": "https://adiyaman.diyanet.gov.tr/tut/Sayfalar/home.aspx"},
    ],
    "Afyonkarahisar": [
        {"ad": "Başmakçı", "url": "https://afyonkarahisar.diyanet.gov.tr/basmakci/Sayfalar/home.aspx"},
        {"ad": "Bayat", "url": "https://afyonkarahisar.diyanet.gov.tr/bayat/Sayfalar/home.aspx"},
        {"ad": "Bolvadin", "url": "https://afyonkarahisar.diyanet.gov.tr/bolvadin/Sayfalar/home.aspx"},
        {"ad": "Çay", "url": "https://afyonkarahisar.diyanet.gov.tr/cay/Sayfalar/home.aspx"},
        {"ad": "Çobanlar", "url": "https://afyonkarahisar.diyanet.gov.tr/cobanlar/Sayfalar/home.aspx"},
        {"ad": "Dazkırı", "url": "https://afyonkarahisar.diyanet.gov.tr/dazkiri/Sayfalar/home.aspx"},
        {"ad": "Dinar", "url": "https://afyonkarahisar.diyanet.gov.tr/dinar/Sayfalar/home.aspx"},
        {"ad": "Emirdağ", "url": "https://afyonkarahisar.diyanet.gov.tr/emirdag/Sayfalar/home.aspx"},
        {"ad": "Evciler", "url": "https://afyonkarahisar.diyanet.gov.tr/evciler/Sayfalar/home.aspx"},
        {"ad": "Hocalar", "url": "https://afyonkarahisar.diyanet.gov.tr/hocalar/Sayfalar/home.aspx"},
        {"ad": "İhsaniye", "url": "https://afyonkarahisar.diyanet.gov.tr/ihsaniye/Sayfalar/home.aspx"},
        {"ad": "İscehisar", "url": "https://afyonkarahisar.diyanet.gov.tr/iscehisar/Sayfalar/home.aspx"},
        {"ad": "Kızılören", "url": "https://afyonkarahisar.diyanet.gov.tr/kiziloren/Sayfalar/home.aspx"},
        {"ad": "Sandıklı", "url": "https://afyonkarahisar.diyanet.gov.tr/sandikli/Sayfalar/home.aspx"},
        {"ad": "Sinanpaşa", "url": "https://afyonkarahisar.diyanet.gov.tr/sinanpasa/Sayfalar/home.aspx"},
        {"ad": "Sultandağı", "url": "https://afyonkarahisar.diyanet.gov.tr/sultandagi/Sayfalar/home.aspx"},
        {"ad": "Şuhut", "url": "https://afyonkarahisar.diyanet.gov.tr/suhut/Sayfalar/home.aspx"},
    ],
    "Ağrı": [
        {"ad": "Diyadin", "url": "https://agri.diyanet.gov.tr/diyadin/Sayfalar/home.aspx"},
        {"ad": "Doğubayazıt", "url": "https://agri.diyanet.gov.tr/dogubayazit/Sayfalar/home.aspx"},
        {"ad": "Eleşkirt", "url": "https://agri.diyanet.gov.tr/eleskirt/Sayfalar/home.aspx"},
        {"ad": "Hamur", "url": "https://agri.diyanet.gov.tr/hamur/Sayfalar/home.aspx"},
        {"ad": "Patnos", "url": "https://agri.diyanet.gov.tr/patnos/Sayfalar/home.aspx"},
        {"ad": "Taşlıçay", "url": "https://agri.diyanet.gov.tr/taslicay/Sayfalar/home.aspx"},
        {"ad": "Tutak", "url": "https://agri.diyanet.gov.tr/tutak/Sayfalar/home.aspx"},
    ],
    "Ankara": [
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
        {"ad": "Evren", "url": "https://ankara.diyanet.gov.tr/evren/Sayfalar/home.aspx"},
        {"ad": "Gölbaşı", "url": "https://ankara.diyanet.gov.tr/golbasi/Sayfalar/home.aspx"},
        {"ad": "Güdül", "url": "https://ankara.diyanet.gov.tr/gudul/Sayfalar/home.aspx"},
        {"ad": "Haymana", "url": "https://ankara.diyanet.gov.tr/haymana/Sayfalar/home.aspx"},
        {"ad": "Keçiören", "url": "https://ankara.diyanet.gov.tr/kecioren/Sayfalar/home.aspx"},
        {"ad": "Kızılcahamam", "url": "https://ankara.diyanet.gov.tr/kizilcahamam/Sayfalar/home.aspx"},
        {"ad": "Mamak", "url": "https://ankara.diyanet.gov.tr/mamak/Sayfalar/home.aspx"},
        {"ad": "Nallıhan", "url": "https://ankara.diyanet.gov.tr/nallihan/Sayfalar/home.aspx"},
        {"ad": "Polatlı", "url": "https://ankara.diyanet.gov.tr/polatli/Sayfalar/home.aspx"},
        {"ad": "Pursaklar", "url": "https://ankara.diyanet.gov.tr/pursaklar/Sayfalar/home.aspx"},
        {"ad": "Sincan", "url": "https://ankara.diyanet.gov.tr/sincan/Sayfalar/home.aspx"},
        {"ad": "Şereflikoçhisar", "url": "https://ankara.diyanet.gov.tr/sereflikochisar/Sayfalar/home.aspx"},
        {"ad": "Yenimahalle", "url": "https://ankara.diyanet.gov.tr/yenimahalle/Sayfalar/home.aspx"},
    ],
    "İstanbul": [
        {"ad": "Beşiktaş", "url": "https://istanbul.diyanet.gov.tr/besiktas/Sayfalar/home.aspx"},
        {"ad": "Fatih", "url": "https://istanbul.diyanet.gov.tr/fatih/Sayfalar/home.aspx"},
        {"ad": "Üsküdar", "url": "https://istanbul.diyanet.gov.tr/uskudar/Sayfalar/home.aspx"},
        {"ad": "Kadıköy", "url": "https://istanbul.diyanet.gov.tr/kadikoy/Sayfalar/home.aspx"},
        # ... Diğer İstanbul ilçelerini buraya ekleyebilirsin
    ],
    # Liste bu şekilde tüm iller için devam ediyor...
}

# --- TEMEL SAYFA FONKSİYONLARI ---

def anasayfa(request):
    return render(request, 'anasayfa.html')

def muftulukler(request):
    # İlleri alfabetik sırala
    iller = sorted(MUFTULUK_VERISI.keys())
    return render(request, 'muftulukler.html', {'iller': iller})

def muftuluk_il(request, il):
    # URL'den gelen il ismini bul (Örn: /muftulukler/Ankara/)
    # Kullanıcı küçük harf yazsa bile (ankara) bulması için düzenliyoruz
    bulunan_il = None
    for key in MUFTULUK_VERISI.keys():
        if key.lower() == il.lower():
            bulunan_il = key
            break
            
    if bulunan_il:
        ilceler = MUFTULUK_VERISI[bulunan_il]
        il_linki = f"https://{bulunan_il.lower().replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}.diyanet.gov.tr/Sayfalar/home.aspx"
    else:
        ilceler = []
        il_linki = "#"

    return render(request, 'muftuluk_il.html', {
        'il': bulunan_il or il,
        'ilceler': ilceler,
        'il_linki': il_linki
    })

# --- DİĞER FONKSİYONLARIN (Giriş, Kayıt vb.) BOŞ HALLERİ ---
# Kendi projene göre bunları doldurabilirsin.

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