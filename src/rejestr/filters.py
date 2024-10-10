import django_filters
from .models import CzynnoscPrzetwarzania

class CzynnoscPrzetwarzaniaFilter(django_filters.FilterSet):

    class meta:
        model = CzynnoscPrzetwarzania
        fields = {
            'czn_active': ['exact'],
            'czn_status_zatw': ['exact'],
            'czn_nazwa': ['icontains', 'istarswith'],
            # "czn_zrodlo_danych",
            # "czn_przepis_wrazliwe",
            # "czn_podstawa_prawna",
            # "czn_opis_celu",
           # "czn_data_zgloszenia": ['exact'],
            # # "czn_data_wyrejestrowania", 
            # "czn_data_obowazywania_od", 
            # "czn_data_obowazywania_do", 
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
        }

        