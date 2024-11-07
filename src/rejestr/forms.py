from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib.auth import get_user_model
from django.contrib.auth import user_logged_in
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

from rejestr.models import ROLA_PRACOWNIKA, STATUS_ZATWIERDZENIA, ZRODLA_DANYCH, ZAKRES_REJESTRACJI, Organizacja

from . import models

class OrganizacjaForm(forms.ModelForm):
    org_active = forms.BooleanField(label='Aktywna', required=False, initial=True)
    
    org_nazwa = forms.CharField(label='Nazwa organizacji', max_length=150, min_length=6, 
                                widget=forms.TextInput(attrs={"placeholder": 'Pełna nazwa organizacji'}),
                                required=True
                                )

    org_skrot = forms.CharField(label='Nazwa skrótowa organizacji', max_length=30, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'Literowy skrót organizacji'}),
                                required=True
                                )

    org_adres = forms.CharField(label='Adres organizacji', max_length=100, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'Pełny adres organizacji'}),
                                required=True
                                )
    
    org_www = forms.CharField(label='Strona www organizacji', max_length=100, min_length=12, 
                                widget=forms.TextInput(attrs={"placeholder": 'http:// ... strona www organizacji'}),
                                required=False
                                )

    org_tel = forms.CharField(label='Telefon kontaktowy organizacji', max_length=100, min_length=12, 
                                widget=forms.TextInput(attrs={"placeholder": 'Telefon kontaktowy organizacji'}),
                                required=False
                                )

    org_email = forms.CharField(label='e-mail organizacji', max_length=100, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'e-mail kontaktowy'}),
                                required=False
                                )

    org_iod_name = forms.CharField(label='Dane IOD organizacji', max_length=100, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'Dane IOD organizacji'}),
                                required=False
                                )

    org_iod_email = forms.CharField(label='e-mail kontaktowy IOD organizacji', max_length=50, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'e-mail kontaktowy IOD organizacji'}),
                                required=False
                                )

    class Meta:
        model = models.Organizacja
        fields = [
            "org_nazwa",
            "org_skrot",
            "org_kod",
            "org_active",
            "org_adres",
            "org_www",
            "org_tel",
            "org_email",
            "org_iod_name",
            "org_iod_email",
        ]

class PodmiotPrzetwarzajacyForm(forms.ModelForm):
    prz_active = forms.BooleanField(label='Aktywny', required=False, initial=True)
    
    prz_nazwa = forms.CharField(label='Nazwa podmiotu', max_length=150, min_length=6, 
                                widget=forms.TextInput(attrs={"placeholder": 'Pełna nazwa podmiotu'}),
                                required=True
                                )

    prz_skrot = forms.CharField(label='Nazwa skrótowa podmiotu', max_length=30, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'Literowy skrót podmiotu'}),
                                required=True
                                )

    prz_adres = forms.CharField(label='Adres podmiotu', max_length=100, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'Pełny adres podmiotu'}),
                                required=True
                                )
    
    prz_www = forms.CharField(label='Strona www podmiotu', max_length=100, min_length=12, 
                                widget=forms.TextInput(attrs={"placeholder": 'http:// ... strona www podmiotu'}),
                                required=False
                                )

    prz_tel = forms.CharField(label='Telefon kontaktowy podmiotu', max_length=100, min_length=12, 
                                widget=forms.TextInput(attrs={"placeholder": 'Telefon kontaktowy podmiotu'}),
                                required=False
                                )

    prz_email = forms.CharField(label='e-mail podmiotu', max_length=100, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'e-mail kontaktowy'}),
                                required=False
                                )

    prz_iod_name = forms.CharField(label='Dane IOD podmiotu', max_length=100, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'Dane IOD podmiotu'}),
                                required=False
                                )

    prz_iod_email = forms.CharField(label='e-mail kontaktowy IOD podmiotu', max_length=50, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'e-mail kontaktowy IOD podmiotu'}),
                                required=False
                                )

    class Meta:
        model = models.PodmiotPrzetwarzajacy
        fields = [
            "prz_nazwa",
            "prz_skrot",
            "prz_active",
            "prz_adres",
            "prz_www",
            "prz_tel",
            "prz_email",
            "prz_iod_name",
            "prz_iod_email",
        ]

class RejestrForm(forms.ModelForm):
    rej_active = forms.BooleanField(label='Aktywny', required=False, initial=True)
    
    rej_nazwa = forms.CharField(label='Nazwa rejestru', max_length=200, min_length=6, 
                                widget=forms.TextInput(attrs={"placeholder": 'Pełna nazwa rejestru'}),
                                required=True
                                )
    rej_opis = forms.CharField(label='Opis rejestru', max_length=200, min_length=6, 
                                widget=forms.Textarea(attrs={"placeholder": 'Opis rejestru'}),
                                required=True
                                )
    
    rej_zakres = forms.ChoiceField(label='Zakres rejestru', 
                                choices=ZAKRES_REJESTRACJI,
                                required=True
                                )

    Organizacja = forms.ModelChoiceField(
                                label="Organizacja", 
                                widget=forms.Select,   
                                queryset=models.Organizacja.objects.filter(org_active = True)
                                )
    
    class Meta:
        model = models.Rejestr
        fields = [
            "rej_active",
            "rej_nazwa",
            "rej_opis",
            "rej_zakres",
            "Organizacja",
        ]

    def __init__(self, *args, **kwargs):
        super(RejestrForm, self).__init__(*args, **kwargs)
        #self.fields["Organizacja"].queryset = models.Organizacja.objects.filter(org_active = True)


class ProfileForm(LoginRequiredMixin, forms.ModelForm):
    
    pro_user = forms.CharField(label='login', max_length=255,  
                        widget=forms.TextInput(attrs={"placeholder": 'Nazwa użytkownika'}),
                        disabled=True,
                        required=True
                        )
    
    pro_nazwa = forms.CharField(label='Nazwa użytkownika', max_length=255,  
                        widget=forms.TextInput(attrs={"placeholder": 'Pełna nazwa użytkownika'}),
                        required=True
                        )
    
    pro_opis = forms.CharField(label='Opis profilu użytkownika', max_length=200, 
                        widget=forms.TextInput(attrs={"placeholder": 'Opis profilu użytkownika'}),
                        required=False
                        )
       
    pro_rola = forms.ChoiceField(label='Status', choices=ROLA_PRACOWNIKA,                
                        required=False) 

    pro_organizacja = forms.ModelChoiceField(
                        required=True,
                        initial='',
                        queryset = models.Organizacja.objects.filter(org_active = True),
                        widget=forms.Select
                        )

    pro_komorka = forms.ModelChoiceField(
                        required=True,
                        initial='',
                        queryset = models.Komorka.objects.filter(kom_active = True),
                        widget=forms.Select
                        )
    
    # pro_avatar = forms.FilePathField(
    #                         widget = forms.FileInput,
    #                     )
       
class KomorkaForm(forms.ModelForm):
    kom_active = forms.BooleanField(label='Aktywna', required=False, initial=True)
    
    kom_nazwa = forms.CharField(label='Nazwa komórki', max_length=255,  
                            widget=forms.TextInput(attrs={"placeholder": 'Pełna nazwa komórki'}),
                            required=True
                            )

    kom_symbol = forms.CharField(label='Skrót komórki', max_length=30,
                                widget=forms.TextInput(attrs={"placeholder": 'Literowy skrót komórki'}),
                                required=True
                                )
    
    kom_adres = forms.CharField(label='Adres komórki', max_length=100,  
                                widget=forms.TextInput(attrs={"placeholder": 'Pełny adres komórki'}),
                                required=False
                                )
    
    kom_tel = forms.CharField(label='Telefon kontaktowy', max_length=100,  
                                widget=forms.TextInput(attrs={"placeholder": 'Telefon kontaktowy'}),
                                required=False
                                )
    kom_email = forms.CharField(label='e-mail komórki', max_length=100, min_length=2, 
                                widget=forms.TextInput(attrs={"placeholder": 'e-mail kontaktowy'}),
                                required=False
                                )
    
    RejestryKomorki = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.Rejestr.objects.filter(rej_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
    class Meta:
        model = models.Komorka
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(KomorkaForm, self).__init__(*args, **kwargs)
        #self.fields["CzynnoscPrzetwarzania"].queryset = CzynnoscPrzetwarzania.objects.all()
        self.fields["Organizacja"].queryset = models.Organizacja.objects.filter(org_active = True)
        #self.fields["CzynnosciRealizowane"].queryset = models.CzynnoscPrzetwarzania.objects.filter(czn_active = True)
        #self.fields["RejestryKomorki"].queryset = models.RejestryKomorki.objects().all()
        
        
class OkresRetencjiForm(forms.ModelForm):
    okr_active = forms.BooleanField(label='Aktywna', required=False, initial=True)
    
    okr_nazwa = forms.CharField(label='Nazwa okresu retencji', max_length=150, 
                                widget=forms.TextInput(attrs={"placeholder": 'Nazwa okresu retencji'}),
                                required=True
                                )

    okr_opis_okresu = forms.CharField(label='Opis okresu retencji', max_length=200, 
                                widget=forms.TextInput(attrs={"placeholder": 'Opis okresu retencji'}),
                                required=False
                                )
    
    okr_lat_max = forms.IntegerField(label='Maksymalna retencja w latach', 
                                required=False
                                )

    class Meta:
        model = models.OkresRetencji
        fields = [
            "okr_active",
            "okr_nazwa",
            "okr_opis_okresu",
            "okr_lat_max",
        ]

class SposobPrzetwarzaniaForm(forms.ModelForm):
    sp_active = forms.BooleanField(label='Aktywny', required=False, initial=True)
    
    sp_skrot = forms.CharField(label='Nazwa sposobu przetwarzania', max_length=100, 
                                widget=forms.TextInput(attrs={"placeholder": 'Nazwa sposobu przetwarzania'}),
                                required=True
                                )

    sp_opis = forms.CharField(label='Opis sposobu przetwarzania', max_length=300, 
                                widget=forms.Textarea(attrs={"placeholder": 'Opis sposobu przetwarzania'}),
                                required=False
                                )
    

    class Meta:
        model = models.SposobPrzetwarzania
        fields = [
            "sp_active",
            "sp_skrot",
            "sp_opis",
        ]

class KategoriaOsobForm(forms.ModelForm):
    ko_active = forms.BooleanField(label='Aktywna', required=False, initial=True)
    
    ko_skrot = forms.CharField(label='Nazwa kategorii osób', max_length=100, 
                                widget=forms.TextInput(attrs={"placeholder": 'Nazwa skrotowa kategorii osób'}),
                                required=True
                                )

    ko_opis = forms.CharField(label='Opis kategorii osób', max_length=300, 
                                widget=forms.Textarea(attrs={"placeholder": 'Opis kategorii osób'}),
                                required=False
                                )
    

    class Meta:
        model = models.KategoriaOsob
        fields = [
            "ko_active",
            "ko_skrot",
            "ko_opis",
        ]

class KategoriaOdbiorcowForm(forms.ModelForm):
    kto_active = forms.BooleanField(label='Aktywny', required=False, initial=True)
    
    kto_skrot = forms.CharField(label='Nazwa kategorii odbiorców', max_length=100, 
                                widget=forms.TextInput(attrs={"placeholder": 'Kategoria odbiorców'}),
                                required=True
                                )

    kto_opis = forms.CharField(label='Opis kategorii odbiorców', max_length=300, 
                                widget=forms.Textarea(attrs={"placeholder": 'Opis kategorii odbiorców'}),
                                required=False
                                )
    

    class Meta:
        model = models.KategoriaOdbiorcow
        fields = [
            "kto_active",
            "kto_skrot",
            "kto_opis",
        ]

class KategoriaDanychForm(forms.ModelForm):
    kd_active = forms.BooleanField(label='Aktywny', required=False, initial=True)
    kd_dane_szczegolne = forms.BooleanField(label='Dane szczególne', required=False, initial=False)
   
    kd_skrot = forms.CharField(label='Nazwa kategorii danych', max_length=100, 
                                widget=forms.TextInput(attrs={"placeholder": 'Kategoria danych'}),
                                required=True
                                )

    kd_opis = forms.CharField(label='Opis kategorii danych', max_length=300, 
                                widget=forms.Textarea(attrs={"placeholder": 'Opis kategorii danych'}),
                                required=False
                                )
    

    class Meta:
        model = models.KategoriaDanych
        fields = [
            "kd_active",
            "kd_skrot",
            "kd_opis",
            "kd_dane_szczegolne",
        ]

class WysokieRyzykoForm(forms.ModelForm):
    wr_active = forms.BooleanField(label='Aktywny', required=False, initial=True)
    
    wr_skrot = forms.CharField(label='Nazwa przesłanki wysokiego ryzyka', max_length=100, 
                                widget=forms.TextInput(attrs={"placeholder": 'Przesłanka wysokiego ryzyka'}),
                                required=True
                                )

    wr_opis = forms.CharField(label='Opis przesłanki ryzyka', max_length=400, 
                                widget=forms.Textarea(attrs={"placeholder": 'Opis przesłanki ryzyka'}),
                                required=False
                                )
    
    class Meta:
        model = models.WysokieRyzyko
        fields = [
            "wr_active",
            "wr_skrot",
            "wr_opis",
        ]

class CzynnoscPrzetwarzaniaFilterForm(forms.Form):
    czn_nazwa = forms.CharField(label='Nazwa' )
    czn_status_zatw = forms.ChoiceField(label='Status', choices=models.STATUS_ZATWIERDZENIA)    
    czn_active = forms.BooleanField(label='Aktywna')
    
class CzynnoscPrzetwarzaniaForm(forms.ModelForm):
    czn_active = forms.BooleanField(label='Aktywna', required=False, initial=True)
    
    czn_pozycja_rej = forms.IntegerField(label='Numer pozycji rejestru',
                                         required=False,
                                         )
    
    czn_nazwa = forms.CharField(label='Nazwa czynności', max_length=200,  
                        widget=forms.TextInput(attrs={"placeholder": 'Pełna nazwa czynności przetwarzania'}),
                        required=True
                        )
    
    # czn_podstawa_prawna = forms.CharField(label='Podstawa prawna', max_length=200,  
    #                     widget=forms.TextInput(attrs={"placeholder": 'Pełna podstawa prawna przetwarzania'}),
    #                     required=True
    #                     )
    
    czn_data_zgloszenia = forms.DateField(label='Data zgloszenia',
                                          widget=DatePickerInput,
                                          required=False) 
    
    czn_data_wyrejestrowania = forms.DateField(label='Data wyrejestrowania',
                                          widget=DatePickerInput,
                                          required=False) 
     
    czn_data_obowazywania_od = forms.DateField(label='Obowiązuje od',
                                          widget=DatePickerInput,
                                          required=False) 

    
    czn_data_obowazywania_do = forms.DateField(label='Obowiązuje do',
                                            widget=DatePickerInput,
                                            required=False) 
  

    czn_status_zatw = forms.ChoiceField(label='Status', choices=STATUS_ZATWIERDZENIA,                
                        required=False) 
    
    czn_stczn_zrodlo_danych = forms.ChoiceField(label='Źródło danych', 
                        choices=ZRODLA_DANYCH,                
                        required=False
                        )
    
    czn_przepis_wrazliwe = forms.CharField(label='Podstawa prawna przetwarzania danych wrażliwych', max_length=200,  
                        widget=forms.TextInput(attrs={"placeholder": 'Podstawa przetwarzania danych wrażliwych'}),
                        required=True
                        )
    
    Rejestr = forms.ModelChoiceField(
                        required=True,
                        initial='',
                        queryset = models.Rejestr.objects.filter(rej_active = True),
                        widget=forms.Select
                        )

    OkresRetencji = forms.ModelChoiceField(
                        required=True,
                        queryset = models.OkresRetencji.objects.filter(okr_active = True),
                        widget=forms.Select
                        )
 
    Administratorzy = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.Organizacja.objects.filter(org_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
    
    Wspoladministratorzy = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.Organizacja.objects.filter(org_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
    
    PodmiotyPrzetwarzajace = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.PodmiotPrzetwarzajacy.objects.filter(prz_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
    

    PrzeslankiLegalnosci = forms.ModelMultipleChoiceField(
                        label='Przełanki legalnosci', 
                        required=False,
                        queryset = models.PrzeslankaLegalnosci.objects.filter(prl_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
    
    PodstawyPrawnePrzetwarzania = forms.ModelMultipleChoiceField(
                        label='Podstawy prawne przetwarzania', 
                        required=False,
                        queryset = models.PodstawaPrawnaPrzetwarzania.objects.filter(ppw_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
 
    
    SposobyPrzetwarzania = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.SposobPrzetwarzania.objects.filter(sp_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )

    OperacjePrzetwarzania = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.OperacjaPrzetwarzania.objects.filter(opp_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
 
    KategorieOsob = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.KategoriaOsob.objects.filter(ko_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
    
    KategorieOdbiorcow = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.KategoriaOdbiorcow.objects.filter(kto_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
    
    KategorieDanych = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.KategoriaDanych.objects.filter(kd_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
    
    WysokieRyzyka = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.WysokieRyzyko.objects.filter(wr_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
    
    KomorkiRealizujace = forms.ModelMultipleChoiceField(
                        required=False,
                        queryset = models.Komorka.objects.filter(kom_active = True),
                        widget=forms.CheckboxSelectMultiple
                        )
    
        
    class Meta:
        model = models.CzynnoscPrzetwarzania
        fields = '__all__'

class CzynnoscPrzetwarzaniaRODOForm(CzynnoscPrzetwarzaniaForm):
   
    class Meta:
        fields = '__all__'
        model = models.CzynnoscPrzetwarzaniaRODO
        proxy = True
    

class KategoriaCzynnosciPrzetwarzaniaRODOForm(CzynnoscPrzetwarzaniaForm):
    
    class Meta:
        fields = '__all__'
        model = models.KategoriaCzynnosciPrzetwarzaniaRODO
        proxy = True


class CzynnoscPrzetwarzaniaDODOForm(CzynnoscPrzetwarzaniaForm):
    class Meta:
        fields = '__all__'
        model = models.CzynnoscPrzetwarzaniaDODO
        proxy = True

class KategoriaCzynnosciPrzetwarzaniaDODOForm(CzynnoscPrzetwarzaniaForm):
    class Meta:
        fields = '__all__'
        model = models.KategoriaCzynnosciPrzetwarzaniaDODO
        proxy = True


class OperacjaPrzetwarzaniaForm(forms.ModelForm):
    opp_active = forms.BooleanField(label='Aktywna', required=False, initial=True)
    
    opp_opis = forms.CharField(label='Opis', max_length=100,  
                        widget=forms.TextInput(attrs={"placeholder": 'Opis operacji'}),
                        required=True
                        )

    class Meta:
        model = models.OperacjaPrzetwarzania
        fields = [
            "opp_active",
            "opp_opis",
        ]
        

class PrzeslankaLegalnosciForm(forms.ModelForm):
    prl_active = forms.BooleanField(label='Aktywna', required=False, initial=True)
    
    prl_skrot = forms.CharField(label='Nazwa skrótowa', max_length=100,  
                        widget=forms.TextInput(attrs={"placeholder": 'Nazwa skrótowa'}),
                        required=True
                        )
    
    prl_art_rodo = forms.CharField(label='Wskazanie artykułu RODO', max_length=100,  
                        widget=forms.TextInput(attrs={"placeholder": 'Artykuł RODO'}),
                        required=True
                        )

    prl_przepis_rodo = forms.CharField(label='Brzmienie przepisu RODO', max_length=500,  
                        widget=forms.Textarea(attrs={"placeholder": 'Treść przepisu RODO'}),
                        required=False
                        )

    class Meta:
        model = models.PrzeslankaLegalnosci
        fields = [
            "prl_active",
            "prl_skrot",
            "prl_art_rodo",
            "prl_przepis_rodo",
        ]
        

class GrupaZagrozenForm(forms.ModelForm):
    gzg_active = forms.BooleanField(label='Aktywna', required=False)
    gzg_opis = forms.CharField(label='Opis grupy zagrożeń', max_length=300, 
                                widget=forms.Textarea(attrs={"placeholder": 'Opis grupy zagrożeń'}),
                                required=False
                                )
    

    class Meta:
        model = models.GrupaZagrozen
        fields = [
            "gzg_active",
            "gzg_opis",
        ]

class GrupaZabezpieczenForm(forms.ModelForm):
    gzb_active = forms.BooleanField(label='Aktywna', required=False, initial=True)
    gzb_opis = forms.CharField(label='Opis grupy zabezpieczeń', max_length=300, 
                                widget=forms.Textarea(attrs={"placeholder": 'Grupa'}),
                                required=False
                                )
    

    class Meta:
        model = models.GrupaZabezpieczen
        fields = [
            "gzb_active",
            "gzb_opis",
        ]

    def __init__(self, *args, **kwargs):
        super(GrupaZabezpieczenForm, self).__init__(*args, **kwargs)

class ZagrozenieForm(forms.ModelForm):
    zag_active = forms.BooleanField(label='Aktywne', required=False, initial=True)
    zag_skrot = forms.CharField(label='Symbol skrótowy', max_length=100, 
                                widget=forms.TextInput(attrs={"placeholder": 'Symbol'}),
                                required=True
                                )

    zag_opis = forms.CharField(label='Opis zagrożenia', max_length=300, 
                                widget=forms.Textarea(attrs={"placeholder": 'Opis zagrożenia'}),
                                required=False
                                )
    GrupaZagrozen = forms.ModelChoiceField(
                                    label='Grupa zagrożeń', 
                                    required=False,
                                    widget=forms.Select,   
                                    queryset=models.GrupaZagrozen.objects.filter(gzg_active = True)
                                    )
    # GrupaZagrozen = forms.ModelMultipleChoiceField(
    #                         label='Grupy zagrożeń', 
    #                         required=False,
    #                         queryset=models.GrupaZagrozen.objects.filter(gzg_active = True),
    #                         widget=forms.CheckboxSelectMultiple
    #                         )


    class Meta:
        model = models.Zagrozenie
        fields = [
            "zag_active",
            "zag_skrot",
            "zag_opis",
            "GrupaZagrozen",
        ]
        
    def __init__(self, *args, **kwargs):
        super(ZagrozenieForm, self).__init__(*args, **kwargs)


class ZabezpieczenieForm(forms.ModelForm):
    zab_active = forms.BooleanField(label='Aktywne', required=False, initial=True)
    zab_skrot = forms.CharField(label='Symbol skrótowy', max_length=100, 
                                widget=forms.TextInput(attrs={"placeholder": 'Symbol'}),
                                required=True
                                )

    zab_opis = forms.CharField(label='Opis zabezpieczenia', max_length=300, 
                                widget=forms.Textarea(attrs={"placeholder": 'Opis'}),
                                required=False
                                )
    GrupyZabezpieczen = forms.ModelMultipleChoiceField(
                                label='Grupy zabezpieczeń', 
                                required=False,
                                queryset = models.GrupaZabezpieczen.objects.filter(gzb_active = True),
                                widget=forms.CheckboxSelectMultiple
                                )
    
    Odpowiedzialni = forms.ModelMultipleChoiceField(
                                    label='Podmioty odpowiedzialne', 
                                    required=False,
                                    widget=forms.CheckboxSelectMultiple, 
                                    queryset=models.Organizacja.objects.filter(org_active = True)
                                    )
    
    # Odpowiedzialny = forms.ModelChoiceField(
    #                                 label='Podmiot odpowiedzialny', 
    #                                 required=False,
    #                                 widget=forms.Select,   
    #                                 queryset=models.Organizacja.objects.filter(org_active = True)
    #                                 )

    # Zagrozenie = forms.ModelChoiceField(
    #                                 label='Zagrożenie', 
    #                                 required=True,
    #                                 widget=forms.Select,   
    #                                 queryset=models.Zagrozenie.objects.filter(zag_active = True)
    #                                 )

    # Zagrozenia = forms.ModelMultipleChoiceField(
    #                             label='Oddziaływanie na zagrozenia', 
    #                             required=False,
    #                             queryset = models.Zagrozenie.objects.filter(zag_active = True),
    #                             widget=forms.CheckboxSelectMultiple
    #                             )


    class Meta:
        model = models.Zabezpieczenie
        fields = [
            "zab_active",
            "zab_skrot",
            "zab_opis",
            "GrupyZabezpieczen",
            "Odpowiedzialni",
            # "Zagrozenia"
       ]

    def __init__(self, *args, **kwargs):
        super(ZabezpieczenieForm, self).__init__(*args, **kwargs)
        #self.fields["GrupyZabezpieczen"].queryset = models.GrupaZabezpieczen.objects.filter(gzb_active = True)
        #self.fields["Rejestr"].queryset = models.Rejestr.objects.filter(rej_active = True)

class PodatnoscForm(forms.ModelForm):
    pdt_active = forms.BooleanField(label='Aktywna', required=False, initial=True)
    
    pdt_skrot = forms.CharField(label='Symbol skrótowy', max_length=100, 
                            widget=forms.TextInput(attrs={"placeholder": 'Symbol'}),
                            required=True
                            )
    
    pdt_opis = forms.CharField(label='Opis podatności', max_length=300, 
                                widget=forms.Textarea(attrs={"placeholder": 'Opis'}),
                                required=False
                                )
    
    pdt_waga = forms.IntegerField(label='Waga', 
                                  required=True,
                                )
    
    Zagrozenia = forms.ModelMultipleChoiceField(
                                label='Podatność na zagrozenia', 
                                required=False,
                                queryset = models.Zagrozenie.objects.filter(zag_active = True),
                                widget=forms.CheckboxSelectMultiple
                                )

    class Meta:
            model = models.Podatnosc
            fields = [
                "pdt_active",
                "pdt_skrot",
                "pdt_opis",
                "pdt_waga",
                "Zagrozenia",
        ]

    def __init__(self, *args, **kwargs):
        super(PodatnoscForm, self).__init__(*args, **kwargs)

class RyzykoForm(forms.ModelForm):
    rr_prawdopodobienstwo_bp = forms.IntegerField(label='Prawdopodobieństwo bez podatności',
                                required=True, 
                                )
     
    rr_prawdopodobienstwo = forms.IntegerField(label='Prawdopodobieństwo',
                                required=True, 
                                )
    rr_oddzialywanie = forms.IntegerField(label='Oddziaływanie',
                                required=True, 
                                )
     
    rr_ryzyko = forms.IntegerField(label='Oddziaływanie',
                                required=True, 
                                )
    
    

    
         