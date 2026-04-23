from django.contrib import admin
from .models import Ilan, IlanMedya, Favori, Haber, Hutbe

class IlanMedyaInline(admin.TabularInline):
    model = IlanMedya
    extra = 3

class IlanAdmin(admin.ModelAdmin):
    inlines = [IlanMedyaInline]

admin.site.register(Haber)
admin.site.register(Ilan, IlanAdmin)
admin.site.register(Favori)

admin.site.register(Hutbe)
