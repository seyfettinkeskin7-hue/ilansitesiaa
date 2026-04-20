from django.contrib import admin
from django.urls import path
from ilanlar import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.anasayfa),            # ← boş URL artık animasyona gidiyor
    path('anasayfa/', views.anasayfa, name='anasayfa'),    # ← asıl site buraya taşındı
    path('ilan/<int:ilan_id>/', views.detay),
    path('kayit/', views.kayit),
    path('giris/', views.giris, name='giris'),
    path('cikis/', views.cikis),
    path('ilan-ekle/', views.ilan_ekle),
    path('ilan-sil/<int:ilan_id>/', views.ilan_sil),
    path('favori/<int:ilan_id>/', views.favori_ekle),
    path('panel/', views.panel, name='panel'),
    path('panel/haber-ekle/', views.haber_ekle),
    path('panel/haber-sil/<int:haber_id>/', views.haber_sil),
    path('muftulukler/', views.muftulukler),
    path('muftulukler/<str:il>/', views.muftuluk_il),
    path('akademi/', views.akademi),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)