from django.contrib import admin
from .models import Ilan, IlanMedya, Favori, Haber

admin.site.register(Haber)
admin.site.register(Ilan)
admin.site.register(IlanMedya)
admin.site.register(Favori)