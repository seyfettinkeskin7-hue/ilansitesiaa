from django.contrib import admin
from django.urls import path, include
from ilanlar import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('manifest.json', TemplateView.as_view(template_name='manifest.json', content_type='application/json')),
    path('service-worker.js', TemplateView.as_view(template_name='service-worker.js', content_type='application/javascript')),
    path('admin/', admin.site.urls),
    path('', views.anasayfa),            # ← boş URL artık animasyona gidiyor
    path('anasayfa/', views.anasayfa, name='anasayfa'),    # ← asıl site buraya taşındı
    path('ilan/<int:ilan_id>/', views.detay),
    path('kayit/', views.kayit),
    path('giris/', views.giris, name='giris'),
    path('cikis/', views.cikis),
    path('ilan-ekle/', views.ilan_ekle),
    path('ilan-sil/<int:ilan_id>/', views.ilan_sil),
    path('favori/<int:ilan_id>/', views.favori_ekle, name='favori_ekle'),
    path('haber/<int:haber_id>/', views.haber_detay, name='haber_detay'),
    path('favoriler/', views.favorilerim, name='favorilerim'),
    path('panel/', views.panel, name='panel'),
    path('panel/haber-ekle/', views.haber_ekle),
    path('panel/haber-sil/<int:haber_id>/', views.haber_sil),
    path('muftulukler/', views.muftulukler),
    path('muftulukler/<str:il>/', views.muftuluk_il),
    path('akademi/', views.akademi, name='akademi'),
    path('akademi/<int:akademi_id>/', views.akademi_detay, name='akademi_detay'),
    path('gorevli/<int:gorevli_id>/', views.gorevli_detay, name='gorevli_detay'),
    path('ilanlar/', views.tum_ilanlar, name='ilanlar'),
    path('hutbeler/', views.hutbeler, name='hutbeler'),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)