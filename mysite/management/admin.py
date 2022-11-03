from django.contrib import admin
from .models import (Projektas,
                     Klientas,
                     Darbuotojas,
                     Darbas,
                     Saskaita)

class ProjektasAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas','pradziosdata', 'pabaigosdata', 'vadovas')
    list_filter = ('pavadinimas','pradziosdata', 'pabaigosdata')
    search_fields = ('pavadinimas','pradziosdata', 'pabaigosdata')

class KlientasAdmin(admin.ModelAdmin):
    list_display = ('vardaspavarde','imone', 'kontaktai')
    list_filter = ('vardaspavarde','imone', 'kontaktai')
    search_fields = ('vardaspavarde','imone', 'kontaktai')

class DarbuotojasAdmin(admin.ModelAdmin):
    list_display = ('vardaspavarde2', 'pareigos')
    list_filter = ('vardaspavarde2', 'pareigos')
    search_fields = ('vardaspavarde2', 'pareigos')

class SaskaitaAdmin(admin.ModelAdmin):
    list_display = ('data', 'suma')
    list_filter = ('data', 'suma')

class DarbasAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas2', 'pastabos')
    list_filter = ('pavadinimas2', 'pastabos')
    search_fields = ('pavadinimas2', 'pastabos')

# Register your models here.
admin.site.register(Projektas, ProjektasAdmin)
admin.site.register(Klientas, KlientasAdmin)
admin.site.register(Darbuotojas, DarbuotojasAdmin)
admin.site.register(Darbas, DarbasAdmin)
admin.site.register(Saskaita, SaskaitaAdmin)