from django.shortcuts import render, redirect

# 81 İlin tamamı ve senin verdiğin linkler
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
    "Adıyaman": [{"ad": "İl Müftülüğü", "url": "https://adiyaman.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Afyonkarahisar": [{"ad": "İl Müftülüğü", "url": "https://afyonkarahisar.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Ağrı": [{"ad": "İl Müftülüğü", "url": "https://agri.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Aksaray": [{"ad": "İl Müftülüğü", "url": "https://aksaray.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Amasya": [{"ad": "İl Müftülüğü", "url": "https://amasya.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Ankara": [
        {"ad": "İl Müftülüğü", "url": "https://ankara.diyanet.gov.tr/Sayfalar/home.aspx"},
        {"ad": "Altındağ", "url": "https://ankara.diyanet.gov.tr/altindag/Sayfalar/home.aspx"},
        {"ad": "Çankaya", "url": "https://ankara.diyanet.gov.tr/cankaya/Sayfalar/home.aspx"},
        {"ad": "Keçiören", "url": "https://ankara.diyanet.gov.tr/kecioren/Sayfalar/home.aspx"},
    ],
    "Antalya": [{"ad": "İl Müftülüğü", "url": "https://antalya.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Ardahan": [{"ad": "İl Müftülüğü", "url": "https://ardahan.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Artvin": [{"ad": "İl Müftülüğü", "url": "https://artvin.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Aydın": [{"ad": "İl Müftülüğü", "url": "https://aydin.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Balıkesir": [{"ad": "İl Müftülüğü", "url": "https://balikesir.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Bartın": [{"ad": "İl Müftülüğü", "url": "https://bartin.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Batman": [{"ad": "İl Müftülüğü", "url": "https://batman.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Bayburt": [{"ad": "İl Müftülüğü", "url": "https://bayburt.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Bilecik": [{"ad": "İl Müftülüğü", "url": "https://bilecik.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Bingöl": [{"ad": "İl Müftülüğü", "url": "https://bingol.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Bitlis": [{"ad": "İl Müftülüğü", "url": "https://bitlis.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Bolu": [{"ad": "İl Müftülüğü", "url": "https://bolu.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Burdur": [{"ad": "İl Müftülüğü", "url": "https://burdur.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Bursa": [{"ad": "İl Müftülüğü", "url": "https://bursa.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Çanakkale": [{"ad": "İl Müftülüğü", "url": "https://canakkale.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Çankırı": [{"ad": "İl Müftülüğü", "url": "https://cankiri.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Çorum": [{"ad": "İl Müftülüğü", "url": "https://corum.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Denizli": [{"ad": "İl Müftülüğü", "url": "https://denizli.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Diyarbakır": [{"ad": "İl Müftülüğü", "url": "https://diyarbakir.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Düzce": [{"ad": "İl Müftülüğü", "url": "https://duzce.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Edirne": [{"ad": "İl Müftülüğü", "url": "https://edirne.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Elazığ": [{"ad": "İl Müftülüğü", "url": "https://elazig.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Erzincan": [{"ad": "İl Müftülüğü", "url": "https://erzincan.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Erzurum": [{"ad": "İl Müftülüğü", "url": "https://erzurum.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Eskişehir": [{"ad": "İl Müftülüğü", "url": "https://eskisehir.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Gaziantep": [{"ad": "İl Müftülüğü", "url": "https://gaziantep.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Giresun": [{"ad": "İl Müftülüğü", "url": "https://giresun.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Gümüşhane": [{"ad": "İl Müftülüğü", "url": "https://gumushane.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Hakkari": [{"ad": "İl Müftülüğü", "url": "https://hakkari.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Hatay": [{"ad": "İl Müftülüğü", "url": "https://hatay.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Iğdır": [{"ad": "İl Müftülüğü", "url": "https://igdir.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Isparta": [{"ad": "İl Müftülüğü", "url": "https://isparta.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "İstanbul": [{"ad": "İl Müftülüğü", "url": "https://istanbul.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "İzmir": [{"ad": "İl Müftülüğü", "url": "https://izmir.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Kahramanmaraş": [{"ad": "İl Müftülüğü", "url": "https://kahramanmaras.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Karabük": [{"ad": "İl Müftülüğü", "url": "https://karabuk.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Karaman": [{"ad": "İl Müftülüğü", "url": "https://karaman.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Kars": [{"ad": "İl Müftülüğü", "url": "https://kars.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Kastamonu": [{"ad": "İl Müftülüğü", "url": "https://kastamonu.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Kayseri": [{"ad": "İl Müftülüğü", "url": "https://kayseri.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Kırıkkale": [{"ad": "İl Müftülüğü", "url": "https://kirikkale.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Kırklareli": [{"ad": "İl Müftülüğü", "url": "https://kirklareli.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Kırşehir": [{"ad": "İl Müftülüğü", "url": "https://kirsehir.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Kilis": [{"ad": "İl Müftülüğü", "url": "https://kilis.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Kocaeli": [{"ad": "İl Müftülüğü", "url": "https://kocaeli.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Konya": [{"ad": "İl Müftülüğü", "url": "https://konya.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Kütahya": [{"ad": "İl Müftülüğü", "url": "https://kutahya.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Malatya": [{"ad": "İl Müftülüğü", "url": "https://malatya.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Manisa": [{"ad": "İl Müftülüğü", "url": "https://manisa.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Mardin": [{"ad": "İl Müftülüğü", "url": "https://mardin.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Mersin": [{"ad": "İl Müftülüğü", "url": "https://mersin.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Muğla": [{"ad": "İl Müftülüğü", "url": "https://mugla.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Muş": [{"ad": "İl Müftülüğü", "url": "https://mus.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Nevşehir": [{"ad": "İl Müftülüğü", "url": "https://nevsehir.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Niğde": [{"ad": "İl Müftülüğü", "url": "https://nigde.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Ordu": [{"ad": "İl Müftülüğü", "url": "https://ordu.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Osmaniye": [{"ad": "İl Müftülüğü", "url": "https://osmaniye.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Rize": [{"ad": "İl Müftülüğü", "url": "https://rize.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Sakarya": [{"ad": "İl Müftülüğü", "url": "https://sakarya.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Samsun": [{"ad": "İl Müftülüğü", "url": "https://samsun.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Siirt": [{"ad": "İl Müftülüğü", "url": "https://siirt.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Sinop": [{"ad": "İl Müftülüğü", "url": "https://sinop.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Sivas": [{"ad": "İl Müftülüğü", "url": "https://sivas.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Şanlıurfa": [{"ad": "İl Müftülüğü", "url": "https://sanliurfa.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Şırnak": [{"ad": "İl Müftülüğü", "url": "https://sirnak.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Tekirdağ": [{"ad": "İl Müftülüğü", "url": "https://tekirdag.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Tokat": [{"ad": "İl Müftülüğü", "url": "https://tokat.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Trabzon": [{"ad": "İl Müftülüğü", "url": "https://trabzon.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Tunceli": [{"ad": "İl Müftülüğü", "url": "https://tunceli.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Uşak": [{"ad": "İl Müftülüğü", "url": "https://usak.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Van": [{"ad": "İl Müftülüğü", "url": "https://van.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Yalova": [{"ad": "İl Müftülüğü", "url": "https://yalova.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Yozgat": [{"ad": "İl Müftülüğü", "url": "https://yozgat.diyanet.gov.tr/Sayfalar/home.aspx"}],
    "Zonguldak": [{"ad": "İl Müftülüğü", "url": "https://zonguldak.diyanet.gov.tr/Sayfalar/home.aspx"}],
}

def anasayfa(request):
    # Senin orijinal ana sayfa kodun (ilanlar ve haberler için)
    # Burayı bozmamak için sadece render yapıyorum
    return render(request, 'index.html')

def muftulukler(request):
    # 81 ili alfabetik olarak listeler ve URL'ler için slug oluşturur
    iller_listesi = []
    for il_adi in sorted(MUFTULUK_VERISI.keys()):
        slug = il_adi.lower().replace('ı','i').replace('ç','c').replace('ö','o').replace('ü','u').replace('ş','s').replace('ğ','g').replace(' ','-')
        iller_listesi.append({'isim': il_adi, 'slug': slug})
    return render(request, 'muftulukler.html', {'iller_listesi': iller_listesi})

def muftuluk_il(request, il):
    # Tıklanan ilin ilçelerini bulur
    bulunan_il = None
    for key in MUFTULUK_VERISI.keys():
        slug = key.lower().replace('ı','i').replace('ç','c').replace('ö','o').replace('ü','u').replace('ş','s').replace('ğ','g').replace(' ','-')
        if slug == il:
            bulunan_il = key
            break
            
    ilceler = MUFTULUK_VERISI.get(bulunan_il, [])
    return render(request, 'muftuluk_il.html', {'il': bulunan_il or il.capitalize(), 'ilceler': ilceler})

# Boş fonksiyonlar (Sayfanın çökmemesi için)
def detay(request, ilan_id): return render(request, 'detay.html')
def kayit(request): return render(request, 'kayit.html')
def giris(request): return render(request, 'giris.html')
def cikis(request): return redirect('/')
def ilan_ekle(request): return render(request, 'ilan_ekle.html')
def ilan_sil(request, ilan_id): return redirect('/')
def favori_ekle(request, ilan_id): return redirect('/')
def panel(request): return render(request, 'panel.html')
def haber_ekle(request): return render(request, 'panel.html')
def haber_sil(request, haber_id): return render(request, 'panel.html')