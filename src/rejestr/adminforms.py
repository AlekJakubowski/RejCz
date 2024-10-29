from django.contrib import admin
from django import forms

from . import models


class CzynnoscPrzetwarzaniaAdminForm(forms.ModelForm):

    class Meta:
        model = models.CzynnoscPrzetwarzania
        fields = "__all__"


class RejestrAdminForm(forms.ModelForm):

    class Meta:
        model = models.Rejestr
        fields = "__all__"


class OrganizacjaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Organizacja
        fields = "__all__"

class PodmiotPrzetwarzajacyAdminForm(forms.ModelForm):

    class Meta:
        model = models.PodmiotPrzetwarzajacy
        fields = "__all__"

class KomorkaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Komorka
        fields = "__all__"

class ProfilUzytkownikaAdminForm(forms.ModelForm):

    class Meta:
        model = models.ProfilUzytkownika
        fields = "__all__"

class OkresRetencjiAdminForm(forms.ModelForm):
    class Meta:
        model = models.OkresRetencji
        fields = "__all__"


class PrzeslankaLegalnosciAdminForm(forms.ModelForm):
    class Meta:
        model = models.PrzeslankaLegalnosci
        fields = "__all__"
    

class SposobPrzetwarzaniaAdminForm(forms.ModelForm):
    class Meta:
        model = models.SposobPrzetwarzania
        fields = "__all__"

class KategoriaDanychAdminForm(forms.ModelForm):
    class Meta:
        model = models.KategoriaDanych
        fields = "__all__"


class KategoriaOdbiorcowAdminForm(forms.ModelForm):
    class Meta:
        model = models.KategoriaOdbiorcow
        fields = "__all__"


class KategoriaOsobAdminForm(forms.ModelForm):
    class Meta:
        model = models.KategoriaOsob
        fields = "__all__"

        
class WysokieRyzykoAdminForm(forms.ModelForm):
    class Meta:
        model = models.WysokieRyzyko
        fields = "__all__"
