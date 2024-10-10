from django.contrib import admin
from . import adminforms

class CzynnoscPrzetwarzaniaAdmin(admin.ModelAdmin):
    form_class = adminforms.CzynnoscPrzetwarzaniaAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "czn_nazwa",
        "czn_active",
        "czn_pozycja_rej",
        "czn_status_zatw",
        "czn_zrodlo_danych",
        "czn_przepis_wrazliwe",
        #"czn_podstawa_prawna",
        "czn_opis_celu",
        "czn_data_zgloszenia",
        "czn_data_wyrejestrowania", 
        "czn_data_obowazywania_od", 
        "czn_data_obowazywania_do", 
        # "Administratorzy",
        # "Wspoladministratorzy",
        # "PodmiotyPrzetwarzajace",
        # "PrzeslankiLegalnosci",
        # "SposobyPrzetwarzania",
        # "KategorieOsob",
        # "KategorieDanych",
        # "KategorieOdbiorcow",
        # "WysokieRyzyka",
        # "OkresRetencji",
        #"Rejestr",
        #"KomorkiRealizujace",
     ]
    readonly_fields = [
        # "czn_active",
        # "czn_pozycja_rej",
        # "czn_status_zatw",
        # "czn_nazwa",
        # "czn_zrodlo_danych",
        # "czn_przepis_wrazliwe",
        # "czn_podstawa_prawna",
        # "czn_opis_celu",
        # "Administratorzy",
        # "Wspoladministratorzy",
        # "PodmiotyPrzetwarzajace",
        # "PrzeslankiLegalnosci",
        # "SposobyPrzetwarzania",
        # "KategorieOsob",
        # "KategorieDanych",
        # "KategorieOdbiorcow",
        # "WysokieRyzyka",
        # "OkresRetencji",
        # "Rejestr",
        # "KomorkiRealizujace",
     ]

class RejestrAdmin(admin.ModelAdmin):
    form_class = adminforms.RejestrAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "rej_active",
        "rej_nazwa",
        "rej_opis",
        "rej_zakres",
        "Organizacja",
    ]
    readonly_fields = [
        # "rej_active",
        # "rej_nazwa",
        # "rej_opis",
        # "rej_zakres",
        # "Organizacja",
        "created",
        "last_updated",
    ]


class OrganizacjaAdmin(admin.ModelAdmin):
    form_class = adminforms.OrganizacjaAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "org_skrot",
        "org_nazwa",
        "org_active",
        "org_adres",
        "org_www",
        "org_tel",
        "org_email",
        "org_iod_name",
        "org_iod_email",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        # "org_iod_name",
        # "org_nazwa",
        # "org_adres",
        # "created",
        # "org_www",
        # "org_tel",
        # "last_updated",
        # "org_iod_email",
        # "org_email",
        # "org_active",
        # "org_skrot",
        "created",
        "last_updated",
    ]

class PodmiotPrzetwarzajacyAdmin(admin.ModelAdmin):
    form_class = adminforms.PodmiotPrzetwarzajacyAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "prz_skrot",
        "prz_nazwa",
        "prz_active",
        "prz_adres",
        "prz_www",
        "prz_tel",
        "prz_email",
        "prz_iod_name",
        "prz_iod_email",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        # "org_iod_name",
        # "org_nazwa",
        # "org_adres",
        # "created",
        # "org_www",
        # "org_tel",
        # "last_updated",
        # "org_iod_email",
        # "org_email",
        # "org_active",
        # "org_skrot",
        "created",
        "last_updated",
    ]

class KomorkaAdmin(admin.ModelAdmin):
    form_class = adminforms.KomorkaAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "kom_symbol",
        "kom_active",
        "kom_nazwa",
        "kom_adres",
        "kom_tel",
        "kom_email",
    ]
    readonly_fields = [
        "created",
        "last_updated",
  ]

class OkresRetencjiAdmin(admin.ModelAdmin):
    form_class = adminforms.OkresRetencjiAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "okr_active",
        "okr_nazwa",
        "okr_opis_okresu",
        "okr_lat_max",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]

class PrzeslankaLegalnosciAdmin(admin.ModelAdmin):
    form_class = adminforms.PrzeslankaLegalnosciAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "prl_skrot",
        "prl_active",
        "prl_art_rodo",
        "prl_przepis_rodo",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
        
class SposobPrzetwarzaniaAdmin(admin.ModelAdmin):
    form_class = adminforms.SposobPrzetwarzaniaAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "sp_skrot",
        "sp_active",
        "sp_opis",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]

class KategoriaDanychAdmin(admin.ModelAdmin):
    form_class = adminforms.KategoriaDanychAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "kd_skrot",
        "kd_active",
        "kd_opis",
        "kd_dane_szczegolne",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class KategoriaOdbiorcowAdmin(admin.ModelAdmin):
    form_class = adminforms.KategoriaOdbiorcowAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "kto_skrot",
        "kto_active",
        "kto_opis",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class KategoriaOsobAdmin(admin.ModelAdmin):
    form_class = adminforms.KategoriaOsobAdminForm
    empty_value_display = "--BRAK DANYCH--"
    list_display = [
        "ko_skrot",
        "ko_active",
        "ko_opis",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class WysokieRyzykoAdmin(admin.ModelAdmin):
    form_class = adminforms.WysokieRyzykoAdminForm
    list_display = [
        "wr_skrot",
        "wr_active",
        "wr_opis",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
      
      
      
      
      