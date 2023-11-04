from rest_framework import viewsets, permissions

from . import serializers
from . import models

# from rejestr.models.komorka import Komorka
# from rejestr.models.organizacja import Organizacja
# from rejestr.models.czynnosc_przetwarzania import CzynnoscPrzetwarzania, STATUS_ZATWIERDZENIA, ZRODLA_DANYCH
# from rejestr.models.okres_retencji import OkresRetencji
# from rejestr.models.rejestr import Rejestr
# from rejestr.models.wysokie_ryzyko import WysokieRyzyko
# from rejestr.models.przeslanka_legalnosci import PrzeslankaLegalnosci
# from rejestr.models.kategoria_odbiorcow import KategoriaOdbiorcow
# from rejestr.models.kategoria_danych import KategoriaDanych
# from rejestr.models.kategoria_osob import KategoriaOsob
# from rejestr.models.sposob_przetwarzania import SposobPrzetwarzania
# from rejestr.models.administratorzy import Administratorzy
# from rejestr.models.podmioty_przetwarzajace import PodmiotyPrzetwarzajace
# from rejestr.models.wspoladministrtorzy import Wspoladministratorzy
# from rejestr.models.czynnosci_przetwarzania import CzynnosciPrzetwarzania
# from rejestr.models.kategorie_danych import KategorieDanych
# from rejestr.models.kategorie_osob import KategorieOsob
# from rejestr.models.kategorie_odbiorcow import KategorieOdbiorcow

class OrganizacjaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Organizacja class"""

    queryset = models.Organizacja.objects.all()
    serializer_class = serializers.OrganizacjaSerializer
    permission_classes = [permissions.IsAuthenticated]


class KomorkaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Komorka class"""

    queryset = models.Komorka.objects.all()
    serializer_class = serializers.KomorkaSerializer
    permission_classes = [permissions.IsAuthenticated]


class RejestrViewSet(viewsets.ModelViewSet):
    """ViewSet for the Rejestr class"""

    queryset = models.Rejestr.objects.all()
    serializer_class = serializers.RejestrSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class CzynnoscPrzetwarzaniaViewSet(viewsets.ModelViewSet):
    """ViewSet for the CzynnoscPrzetwarzania class"""

    queryset = models.CzynnoscPrzetwarzania.objects.all()
    serializer_class = serializers.CzynnoscPrzetwarzaniaSerializer
    permission_classes = [permissions.IsAuthenticated]


class OkresRetencjiViewSet(viewsets.ModelViewSet):
    """ViewSet for the OkresRetencji class"""

    queryset = models.OkresRetencji.objects.all()
    serializer_class = serializers.OkresRetencjiSerializer
    permission_classes = [permissions.IsAuthenticated]


class SposobPrzetwarzaniaViewSet(viewsets.ModelViewSet):
    """ViewSet for the SposobPrzetwarzania class"""

    queryset = models.SposobPrzetwarzania.objects.all()
    serializer_class = serializers.SposobPrzetwarzaniaSerializer
    permission_classes = [permissions.IsAuthenticated]


class KategoriaOsobViewSet(viewsets.ModelViewSet):
    """ViewSet for the KategoriaOsob class"""

    queryset = models.KategoriaOsob.objects.all()
    serializer_class = serializers.KategoriaOsobSerializer
    permission_classes = [permissions.IsAuthenticated]

class KategoriaOdbiorcowViewSet(viewsets.ModelViewSet):
    """ViewSet for the KategoriaOdbiorcow class"""

    queryset = models.KategoriaOdbiorcow.objects.all()
    serializer_class = serializers.KategoriaOdbiorcowSerializer
    permission_classes = [permissions.IsAuthenticated]

class KategoriaDanychViewSet(viewsets.ModelViewSet):
    """ViewSet for the KategoriaDanych class"""

    queryset = models.KategoriaDanych.objects.all()
    serializer_class = serializers.KategoriaDanychSerializer
    permission_classes = [permissions.IsAuthenticated]


class WysokieRyzykoViewSet(viewsets.ModelViewSet):
    """ViewSet for the WysokieRyzyko class"""

    queryset = models.WysokieRyzyko.objects.all()
    serializer_class = serializers.WysokieRyzykoSerializer
    permission_classes = [permissions.IsAuthenticated]


class PrzeslankaLegalnosciViewSet(viewsets.ModelViewSet):
    """ViewSet for the PrzeslankaLegalnosci class"""

    queryset = models.PrzeslankaLegalnosci.objects.all()
    serializer_class = serializers.PrzeslankaLegalnosciSerializer
    permission_classes = [permissions.IsAuthenticated]








