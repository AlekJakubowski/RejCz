from django.contrib import admin
#from django import forms

from . import models
from . import adminmodels



admin.site.register(models.CzynnoscPrzetwarzania, adminmodels.CzynnoscPrzetwarzaniaAdmin)
admin.site.register(models.Rejestr, adminmodels.RejestrAdmin)
admin.site.register(models.Organizacja, adminmodels.OrganizacjaAdmin)
admin.site.register(models.PodmiotPrzetwarzajacy, adminmodels.PodmiotPrzetwarzajacyAdmin)
admin.site.register(models.Komorka, adminmodels.KomorkaAdmin)
admin.site.register(models.SposobPrzetwarzania, adminmodels.SposobPrzetwarzaniaAdmin)
admin.site.register(models.PrzeslankaLegalnosci, adminmodels.PrzeslankaLegalnosciAdmin)
admin.site.register(models.KategoriaOdbiorcow, adminmodels.KategoriaOdbiorcowAdmin)
admin.site.register(models.KategoriaDanych, adminmodels.KategoriaDanychAdmin)
admin.site.register(models.KategoriaOsob, adminmodels.KategoriaOsobAdmin)
admin.site.register(models.WysokieRyzyko, adminmodels.WysokieRyzykoAdmin)
