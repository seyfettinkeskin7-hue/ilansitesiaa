from django.contrib import admin
from .models import Ilan, IlanMedya, Favori, Haber, Hutbe, Akademi, AkademiKategori, AkademiResim, AkademiGorevli, Bildirim

class IlanMedyaInline(admin.TabularInline):
    model = IlanMedya
    extra = 3

def onayla(modeladmin, request, queryset):
    queryset.update(onaylandi=True)
onayla.short_description = "Seçili ilanları onayla"

class IlanAdmin(admin.ModelAdmin):
    inlines = [IlanMedyaInline]
    list_display = ['baslik', 'kullanici', 'tarih', 'onaylandi']
    list_filter = ['onaylandi']
    actions = [onayla]

class OnayBekleyenIlanAdmin(admin.ModelAdmin):
    inlines = [IlanMedyaInline]
    list_display = ['baslik', 'kullanici', 'tarih']
    actions = [onayla]

    def get_queryset(self, request):
        return super().get_queryset(request).filter(onaylandi=False)

    def has_add_permission(self, request):
        return False

class OnayBekleyenIlan(Ilan):
    class Meta:
        proxy = True
        verbose_name = 'Onay Bekleyen İlan'
        verbose_name_plural = 'Onay Bekleyen İlanlar'

class AkademiResimInline(admin.TabularInline):
    model = AkademiResim
    extra = 3

class AkademiAdmin(admin.ModelAdmin):
    inlines = [AkademiResimInline]
    list_display = ['ad', 'kategori', 'sehir', 'aktif', 'sira']
    list_filter = ['kategori', 'aktif']
    list_editable = ['sira', 'aktif']

class AkademiKategoriAdmin(admin.ModelAdmin):
    list_display = ['ad', 'sira']
    list_editable = ['sira']

admin.site.register(Haber)
admin.site.register(Ilan, IlanAdmin)
admin.site.register(OnayBekleyenIlan, OnayBekleyenIlanAdmin)
admin.site.register(Favori)
admin.site.register(Hutbe)
admin.site.register(AkademiKategori, AkademiKategoriAdmin)
admin.site.register(AkademiGorevli)
admin.site.register(Bildirim)
admin.site.register(Akademi, AkademiAdmin)
