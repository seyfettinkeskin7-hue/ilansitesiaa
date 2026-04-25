from django.contrib import admin
from .models import Ilan, IlanMedya, Favori, Haber, Hutbe, Akademi, AkademiKategori, AkademiResim, AkademiGorevli

class IlanMedyaInline(admin.TabularInline):
    model = IlanMedya
    extra = 3

class IlanAdmin(admin.ModelAdmin):
    inlines = [IlanMedyaInline]

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
admin.site.register(Favori)
admin.site.register(Hutbe)
admin.site.register(AkademiKategori, AkademiKategoriAdmin)
admin.site.register(AkademiGorevli)
admin.site.register(Akademi, AkademiAdmin)
