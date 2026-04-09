from django.contrib import admin
from django.urls import path
from ilanlar import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.anasayfa),
    path('ilan/<int:ilan_id>/', views.detay),
    path('kayit/', views.kayit),
    path('giris/', views.giris),
    path('cikis/', views.cikis),
    path('ilan-ekle/', views.ilan_ekle),
    path('ilan-sil/<int:ilan_id>/', views.ilan_sil),
    path('favori/<int:ilan_id>/', views.favori_ekle),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)