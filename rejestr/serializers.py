from rest_framework import serializers

from . import models


class CzynnoscPrzetwarzaniaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CzynnoscPrzetwarzania
        fields = '__all__'
        # fields = [
        #     "czn_active",
        #     "czn_pozycja_rej",
        #     "czn_status_zatw",
        #     "czn_nazwa",
        #     "czn_zrodlo_danych",
        #     "czn_przepis_wrazliwe",
        #     "czn_podstawa_prawna",
        #     "czn_opis_celu",
        #     "czn_data_zgloszenia",
        #     "czn_data_wyrejestrowania", 
        #     "czn_data_obowazywania_od", 
        #     "czn_data_obowazywania_do", 
        #     "Administratorzy",
        #     "Wspoladministratorzy",
        #     "PodmiotyPrzetwarzajace",
        #     "PrzeslankiLegalnosci",
        #     "SposobyPrzetwarzania",
        #     "KategorieOsob",
        #     "KategorieDanych",
        #     "KategorieOdbiorcow",
        #     "WysokieRyzyka",
        #     "OkresRetencji",
        #     "Rejestr",
        #     "KomorkiRealizujace",
        #     "created",
        #     "last_updated",
        # ]

class OrganizacjaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Organizacja
        fields = [
            "org_nazwa",
            "org_skrot",
            "org_active",
            "org_adres",
            "org_www",
            "org_tel",
            "org_email",
            "org_iod_name",
            "org_iod_email",
        ]

        
class RejestrSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rejestr
        fields = [
            "rej_active",
            "rej_nazwa",
            "rej_opis",
            "rej_zakres",
            "Organizacja",
        ]


class KomorkaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Komorka
        fields = [
            "kom_active",
            "kom_symbol",
            "kom_nazwa",
            "kom_adres",
            "kom_tel",
            "kom_email",
            "Organizacja",
            "CzynnosciRealizowane",
        ]


class OkresRetencjiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.OkresRetencji
        fields = [
            "okr_active",
            "okr_nazwa",
            "okr_opis_okresu",
            "okr_lat_max",
        ]

class SposobPrzetwarzaniaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.SposobPrzetwarzania
        fields = [
            "sp_active",
            "sp_skrot",
            "sp_opis",
        ]

class KategoriaOsobSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.KategoriaOsob
        fields = [
            "ko_active",
            "ko_skrot",
            "ko_opis",
        ]


class KategoriaOdbiorcowSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.KategoriaOdbiorcow
        fields = [
            "kto_active",
            "kto_skrot",
            "kto_opis",
        ]


class KategoriaDanychSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.KategoriaDanych
        fields = [
            "kd_active",
            "kd_skrot",
            "kd_opis",
            "kd_dane_szczegolne",
        ]


class WysokieRyzykoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.WysokieRyzyko
        fields = [
            "wr_active",
            "wr_skrot",
            "wr_opis",
        ]


class PrzeslankaLegalnosciSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.PrzeslankaLegalnosci
        fields = [
            "prl_active",
            "prl_skrot",
            "prl_art_rodo",
            "prl_przepis_rodo",
        ]




