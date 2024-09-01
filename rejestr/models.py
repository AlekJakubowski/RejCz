from typing import Any
from django.db import models, transaction
from django.db.models import Max
from django.core.exceptions import ValidationError

from django.shortcuts import get_object_or_404
from django.urls import reverse

STATUS_ZATWIERDZENIA = (
    ("-----------", "-----------"),
    ("OCZEKUJĄCA", "OCZEKUJĄCA"),
    ("ANULOWANA", "ANULOWANA"),
    ("ODRZUCONA", "ODRZUCONA"),
    ("ZATWIERDZONA", "ZATWIERDZONA"),
)

ZRODLA_DANYCH = (
#    ("-----------", "-----------"),
    ("Bezpośrednio od osoby, której dane dotyczą", "Bezpośrednio od osoby, której dane dotyczą"),
    ("Od innej osoby, niż osoba której dane dotyczą", "Od innej osoby, niż osoba której dane dotyczą"),
    ("Od osoby, której dane dotyczą lub od innych osób", "Od osoby, której dane dotyczą lub od innych osób"),
)

class Organizacja(models.Model):
    # Fields
    org_active = models.BooleanField(default=True)
    org_skrot = models.CharField(max_length=30)
    org_nazwa = models.CharField(max_length=155)
    org_adres = models.CharField(max_length=100)
    org_email = models.EmailField(max_length=50)
    org_www = models.URLField(max_length=100)
    org_tel = models.CharField(max_length=100)
    org_iod_name = models.CharField(max_length=100)
    org_iod_email = models.EmailField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        pass
    
    def __str__(self):
        return str(f'{self.org_skrot} - {self.org_nazwa}')

    def get_absolute_url(self):
        return reverse("Organizacja_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Organizacja_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Organizacja_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Organizacja_htmx_delete", args=(self.pk,))

class PodmiotPrzetwarzajacy(models.Model):
    # Fields
    prz_active = models.BooleanField(default=True)
    prz_skrot = models.CharField(max_length=30)
    prz_nazwa = models.CharField(max_length=155)
    prz_adres = models.CharField(max_length=100)
    prz_email = models.EmailField(max_length=50)
    prz_www = models.URLField(max_length=100)
    prz_tel = models.CharField(max_length=100)
    prz_iod_name = models.CharField(max_length=100)
    prz_iod_email = models.EmailField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        pass
    
    def __str__(self):
        return str(f'{self.prz_skrot} - {self.prz_nazwa}')

    def get_absolute_url(self):
        return reverse("PodmiotPrzetwarzajacy_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PodmiotPrzetwarzajacy_update", args=(self.pk,))


class Rejestr(models.Model):

    # Relationships
    Organizacja = models.ForeignKey(Organizacja, null=True, on_delete=models.SET_NULL)

    # Fields
    rej_active = models.BooleanField(default=True)
    rej_nazwa = models.CharField(max_length=200)
    rej_opis = models.TextField(max_length=200)
    rej_zakres = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return f'{self.rej_nazwa} ({self.rej_zakres}) --> ({self.Organizacja})'

    def get_absolute_url(self):
        return reverse("Rejestr_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Rejestr_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Rejestr_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Rejestr_htmx_delete", args=(self.pk,))

class OkresRetencji(models.Model):

    # Fields
    okr_active = models.BooleanField(null=False, default=True)
    okr_nazwa = models.CharField(max_length=255)
    okr_opis_okresu = models.CharField(max_length=200)
    okr_lat_max = models.PositiveIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self) -> str:
        return f'{self.okr_nazwa} --> ({self.okr_opis_okresu}()'
    
    def __unicode__(self):
        return u'%s' % self.okr_nazwa

    def get_absolute_url(self):
        return reverse('OkresRetencji_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('OkresRetencji_update', args=(self.pk,))

class PrzeslankaLegalnosci(models.Model):
    prl_active = models.BooleanField(null=True, default=True)
    prl_skrot = models.CharField(null=False, max_length=100)
    prl_art_rodo = models.CharField(null=False, max_length=100)
    prl_przepis_rodo = models.CharField(null=True, max_length=500)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
     
    class Meta:
        pass

    def __str__(self):
        return f'{self.prl_skrot}'

    def get_absolute_url(self):
        return reverse("PrzeslankaLegalnosci_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PrzeslankaLegalnosci_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("PrzeslankaLegalnosci_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("PrzeslankaLegalnosci_htmx_delete", args=(self.pk,))

class SposobPrzetwarzania(models.Model):

    # Fields
    sp_active = models.BooleanField(default=True)
    sp_skrot = models.CharField(null=False, max_length=100)
    sp_opis = models.CharField(null=True ,max_length=300)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self) -> str:
        return f'{self.sp_skrot}'
    
    def __unicode__(self):
        return u'%s' % self.sp_opis

    def get_absolute_url(self):
        return reverse('SposobPrzetwarzania_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('SposobPrzetwarzania_update', args=(self.pk,))

class KategoriaDanych(models.Model):

    # Fields
    kd_active = models.BooleanField(default=True)
    kd_skrot = models.CharField(max_length=100)
    kd_opis = models.TextField(max_length=300)
    kd_dane_szczegolne = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self) -> str:
        return f'{self.kd_skrot}'
    
    def __unicode__(self):
        return u'%s' % self.kd_opis_danych

    def get_absolute_url(self):
        return reverse('KategoriaDanych_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('KategoriaDanych_update', args=(self.pk,))

class KategoriaOdbiorcow(models.Model):

    # Fields
    kto_active = models.BooleanField(default=True)
    kto_skrot = models.CharField(max_length=100)
    kto_opis = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass
    
    def __str__(self) -> str:
        return f'{self.kto_skrot}'

    def __unicode__(self):
        return u'%s' % self.kto_opis

    def get_absolute_url(self):
        return reverse('KategoriaOdbiorcow_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('KategoriaOdbiorcow_update', args=(self.pk,))

class KategoriaOsob(models.Model):

    # Fields
    ko_active = models.BooleanField(default=True)
    ko_skrot = models.CharField(max_length=100)
    ko_opis = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        pass

    def __str__(self) -> str:
        return f'{self.ko_skrot}'
        
    def __unicode__(self):
        return u'%s' % self.ko_opis

    def get_absolute_url(self):
        return reverse('KategoriaOsob_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('KategoriaOsob_update', args=(self.pk,))

class WysokieRyzyko(models.Model):

    # Fields
    wr_active = models.BooleanField(default=True)
    wr_skrot = models.CharField(max_length=100)
    wr_opis = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        pass
    
    def __str__(self) -> str:
        return f'{self.wr_skrot}'
    
    def __unicode__(self):
        return u'%s' % self.wr_nazwa

    def get_absolute_url(self):
        return reverse('WysokieRyzyko_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('WysokieRyzyko_update', args=(self.pk,))

class Komorka(models.Model):

    # Relationships
    # CzynnoscPrzetwarzania = models.ManyToManyField(CzynnoscPrzetwarzania)

    # Fields
    kom_active = models.BooleanField(default=True)
    kom_symbol = models.CharField(max_length=10)
    kom_nazwa = models.CharField(max_length=255)
    Organizacja = models.ForeignKey(Organizacja, null=True, on_delete=models.SET_NULL)
    kom_adres = models.CharField(max_length=255)
    kom_tel = models.CharField(max_length=100)
    kom_email = models.EmailField()
    
    CzynnosciRealizowane = models.ManyToManyField(
        'rejestr.CzynnoscPrzetwarzania',
        editable=True,
        related_name="Komorki_CzynnosciPrzetwarzania",
        through="CzynnosciPrzetwarzania",
        through_fields=( 'czp_komorka', 'czp_czynnoscp')
    )
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(f'{self.kom_symbol} - {self.kom_nazwa}')

    def get_absolute_url(self):
        return reverse("Komorka_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Komorka_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Komorka_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Komorka_htmx_delete", args=(self.pk,))


class OperacjaPrzetwarzania(models.Model):
    opp_active = models.BooleanField(null=True, default=True)
    opp_opis = models.CharField(null=False, max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return f'{self.opp_opis}'

    def get_absolute_url(self):
        return reverse("OperacjaPrzetwarzania_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("OperacjaPrzetwarzania_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("OperacjaPrzetwarzania_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("OperacjaPrzetwarzania_htmx_delete", args=(self.pk,))


class CzynnoscPrzetwarzania(models.Model):
    class StatusZatwierdzenia():
        ZATWIERDZONA = "ZATWIERDZONA"
        ANULOWANA = "ANULOWANA"
        ODRZUCONA = "ODRZUCONA"
        OCZEKUJACA = "OCZEKUJĄCA"

    # Fields
    czn_active = models.BooleanField(null=True, default=True)
    czn_nazwa = models.CharField(max_length=200)
    czn_zrodlo_danych = models.CharField(max_length=100, null=True, choices=ZRODLA_DANYCH)
    czn_status_zatw = models.CharField(max_length=20, null=True, choices=STATUS_ZATWIERDZENIA)
    Rejestr = models.ForeignKey(Rejestr, null=True, on_delete=models.SET_NULL)
    czn_pozycja_rej = models.IntegerField(null=False)
    czn_przepis_wrazliwe = models.CharField(max_length=200)
    czn_podstawa_prawna = models.CharField(max_length=300)
    czn_opis_celu = models.CharField(max_length=200)
    czn_data_zgloszenia = models.DateField(null=True) 
    czn_data_wyrejestrowania = models.DateField(null=True) 
    czn_data_obowazywania_od = models.DateField(null=True) 
    czn_data_obowazywania_do = models.DateField(null=True) 
    
    Administratorzy = models.ManyToManyField(
        Organizacja,
        editable=True,
        related_name="Organizacja_Administratorzy",
        through="Administratorzy",
        through_fields=("adm_czynnoscp", "adm_organizacja")
        )
    
    OkresRetencji = models.ForeignKey(OkresRetencji, null=True, on_delete=models.SET_NULL)
    
    Wspoladministratorzy = models.ManyToManyField(
        Organizacja,
        editable=True,
        related_name="Organizacja_Wspoladministratorzy",
        through="Wspoladministratorzy",
        through_fields=("wad_czynnoscp", "wad_organizacja")
        )

    PodmiotyPrzetwarzajace = models.ManyToManyField(
        PodmiotPrzetwarzajacy,
        editable=True,
        related_name="PodmiotPrzetw_PodmiotyPrzetwarzajace",
        through="PodmiotyPrzetwarzajace",
        through_fields=("pod_czynnoscp", "pod_organizacja")
        )

    SposobyPrzetwarzania = models.ManyToManyField(
        SposobPrzetwarzania,
        editable=True,
        related_name="CzynnoscPrzetwarzania_SposobyPrzetwarzania",
        through="SposobyPrzetwarzania",
        through_fields=("spp_czynnoscp", "spp_sposobp")
        )
    
    KategorieDanych = models.ManyToManyField(
        KategoriaDanych,
        editable=True,
        related_name="CzynnoscPrzetwarzania_KategoriaDanych",
        through="KategorieDanych",
        through_fields=("ktd_czynnoscp", "ktd_dane")
        )

    KategorieOsob = models.ManyToManyField(
        KategoriaOsob,
        editable=True,
        related_name="CzynnoscPrzetwarzania_KategoriaOsob",
        through="KategorieOsob",
        through_fields=("kos_czynnoscp", "kos_kosoby")
        )

    KategorieOdbiorcow = models.ManyToManyField(
        KategoriaOdbiorcow,
        editable=True,
        related_name="CzynnoscPrzetwarzania_KategoriaOdbiorcow",
        through="KategorieOdbiorcow",
        through_fields=("kob_czynnoscp", "kob_odbiorcy")
        )
  
    WysokieRyzyka = models.ManyToManyField(
        WysokieRyzyko,
        editable=True,
        related_name="CzynnoscPrzetwarzania_WysokieRyzyko",
        through="WysokieRyzyka",
        through_fields=("wrr_czynnoscp", "wrr_wryzyka")
        )
    
    PrzeslankiLegalnosci = models.ManyToManyField(
        PrzeslankaLegalnosci,
        editable=True,
        related_name="CzynnoscPrzetwarzania_PrzeslankaLegalnosci",
        through="PrzeslankiLegalnosci",
        through_fields=("ppl_czynnoscp", "ppl_przeslankap")
        )

    OperacjePrzetwarzania = models.ManyToManyField(
        OperacjaPrzetwarzania,
        editable=True,
        related_name="CzynnoscPrzetwarzania_OperacjePrzetwarzania",
        through="OperacjePrzetwarzania",
        through_fields=("opp_czynnoscp", "opp_operacjap")
        )
    
    KomorkiRealizujace = models.ManyToManyField(
        Komorka,
        editable=True,
        related_name="CzynnoscPrzetwarzania_Komorki",
        through="CzynnosciPrzetwarzania",
        through_fields=('czp_czynnoscp', 'czp_komorka')
        )

    #Zabezpieczenie = models.ForeignKey(Zabezpieczenie, on_delete=models.CASCADE)#("content_type", "object_id")
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
    def get_status_display(self):
        if(self.czn_status_zatw== 'ZATWIERDZONA'):
            return "Zatwierdzona"
        if(self.czn_status_zatw== 'ANULOWANA'):
            return "Anulowana"
        if(self.czn_status_zatw== 'OCZEKUJĄCA'):
            return "Oczekująca"
        if(self.czn_status_zatw== 'ODRZUCONA'):
            return "Odrzucona"
        
        return "Nieznany status"
    
    def save(self, *args, **kwargs):
        if self.pk is None:  # Only calculate numer if the object is new (not yet in the database)
            # Lock the rows in the database to prevent race conditions
            with transaction.atomic():
                # Znajdź maksymalny numer dla danego Rejestru
                rs_max = CzynnoscPrzetwarzania.objects.select_for_update().filter(Rejestr=self.Rejestr).aggregate(max_numer=Max('czn_pozycja_rej'))
                last_poz_rej = rs_max['max_numer']
                if last_poz_rej is None: 
                    # Jesli max numer dla danego Rejestru jest pusty to będzie pierwszy
                    self.czn_pozycja_rej = 1
                else:
                    # Jesli max numer dla danego Rejestru nie jest pusty to będzie natępny
                    self.czn_pozycja_rej = last_poz_rej + 1
        
        super().save(*args, **kwargs)

    def clone(self):
        with transaction.atomic():
            # Pobierz rekord z zadanym pk
            rs_max = CzynnoscPrzetwarzania.objects.select_for_update().filter(Rejestr=self.Rejestr).aggregate(max_numer=Max('czn_pozycja_rej'))
            last_poz_rej = rs_max['max_numer']
            next_poz_rej = last_poz_rej + 1
            # Stwórz nowy obiekt z danymi sklonowanymi z bieżącego obiektu
            new_instance = CzynnoscPrzetwarzania(
                Rejestr=self.Rejestr,
                czn_pozycja_rej = next_poz_rej,
                czn_active = self.czn_active,
                czn_status_zatw = "OCZEKUJĄCA",
                czn_nazwa = "_klon_" + self.czn_nazwa,
                czn_zrodlo_danych = self.czn_zrodlo_danych,
                czn_przepis_wrazliwe = self.czn_przepis_wrazliwe,
                czn_podstawa_prawna = self.czn_podstawa_prawna,
                czn_opis_celu = self.czn_opis_celu,
                czn_data_zgloszenia = self.czn_data_zgloszenia,
                czn_data_wyrejestrowania = None,
                czn_data_obowazywania_od = None,
                czn_data_obowazywania_do = None,
                OkresRetencji = self.OkresRetencji,
                #KomorkiRealizujace = None, #self.KomorkiRealizujace,
                created = None,
                last_updated = None,
            )
            #zapis nowej instancji
            new_instance.save() # sklonowany
            
            Adm_rs = Administratorzy.objects.filter(adm_czynnoscp=self.pk)
            for x in Adm_rs:
                x.clone(new_instance)
            
            WRyz_rs = Wspoladministratorzy.objects.filter(wad_czynnoscp=self.pk)
            for x in WRyz_rs:
                x.clone(new_instance)
            
            PodP_rs = PodmiotyPrzetwarzajace.objects.filter(pod_czynnoscp=self.pk)
            for x in PodP_rs:
                x.clone(new_instance)
            
            PrzeL_rs = PrzeslankiLegalnosci.objects.filter(ppl_czynnoscp=self.pk)
            for x in PrzeL_rs:
                x.clone(new_instance)

            SposP_rs = SposobyPrzetwarzania.objects.filter(spp_czynnoscp=self.pk)
            for x in SposP_rs:
                x.clone(new_instance)
                
            KatOs_rs = KategorieOsob.objects.filter(kos_czynnoscp=self.pk)
            for x in KatOs_rs:
                x.clone(new_instance)
            
            KatDt_rs = KategorieDanych.objects.filter(ktd_czynnoscp=self.pk)
            for x in KatDt_rs:
                x.clone(new_instance)
          
            KatOd_rs = KategorieOdbiorcow.objects.filter(kob_czynnoscp=self.pk)
            for x in KatOd_rs:
                x.clone(new_instance)
          
            WRyz_rs = WysokieRyzyka.objects.filter(wrr_czynnoscp=self.pk)
            for x in WRyz_rs:
                x.clone(new_instance)
            
        return new_instance

    

    class Meta:
        #abstract = True
        pass

    def __str__(self):
        return f'{self.czn_pozycja_rej} {self.czn_nazwa}'

    def get_absolute_url(self):
        return reverse("CzynnoscPrzetwarzania_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("CzynnoscPrzetwarzania_update", args=(self.pk,))

    def get_clone_url(self):
        return reverse("CzynnoscPrzetwarzania_clone", args=(self.pk,))
    
    # @staticmethod
    # def get_htmx_create_url():
    #     return reverse("CzynnoscPrzetwarzania_htmx_create")

    # def get_htmx_delete_url(self):
    #     return reverse("CzynnoscPrzetwarzania_htmx_delete", args=(self.pk,))


class CzynnosciPrzetwarzania(models.Model):
    czp_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania,
                                      null=True,
                                      related_name="czp_czynnosc_p",
                                      on_delete=models.CASCADE)
    czp_komorka = models.ForeignKey(Komorka, 
                                    null=True,
                                    related_name="czp_komorka_p",
                                    on_delete=models.CASCADE)

class Administratorzy(models.Model):
    adm_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania, 
                                        null=True,
                                      related_name="adm_czynnosc_p",
                                      on_delete=models.CASCADE)
    adm_organizacja = models.ForeignKey(Organizacja, 
                                    null=True,
                                    related_name="adm_organizacja_f",
                                    on_delete=models.CASCADE)

    def clone(self, new_czynn):
        new_adm = Administratorzy(
            adm_czynnoscp = new_czynn,
            adm_organizacja = self.adm_organizacja 
        )
        new_adm.save()

    
class Wspoladministratorzy(models.Model):
    wad_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania,
                                    null=True,
                                    related_name="wad_czynnosc_p",
                                    on_delete=models.CASCADE)
    
    wad_organizacja = models.ForeignKey(Organizacja, 
                                    null=True,
                                    related_name="wad_organizacja_f",                                 
                                    on_delete=models.CASCADE)
    
    def clone(self, new_czynn):
        wadm = Wspoladministratorzy(
            wad_czynnoscp = new_czynn,
            wad_organizacja = self.wad_organizacja 
        )
        wadm.save()


class PodmiotyPrzetwarzajace(models.Model):
    pod_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania, 
                                      null=True,
                                      related_name="pod_czynnosc_p",
                                      on_delete=models.CASCADE)
    pod_organizacja = models.ForeignKey(PodmiotPrzetwarzajacy, 
                                    null=True,
                                    related_name="pod_pprzetw_p",
                                    on_delete=models.CASCADE)
    
    def clone(self, new_czynn):
        podp = PodmiotyPrzetwarzajace(
            pod_czynnoscp = new_czynn,
            pod_organizacja = self.pod_organizacja 
        )
        podp.save()


class SposobyPrzetwarzania(models.Model):
    spp_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania, 
                                      null=True,
                                      related_name="spp_czynnosc_p",
                                      on_delete=models.CASCADE)
    
    spp_sposobp = models.ForeignKey(SposobPrzetwarzania, 
                                    null=True,
                                    related_name="spp_sposob_p",
                                    on_delete=models.CASCADE)
   
    def clone(self, new_czynn):
        pop = SposobyPrzetwarzania(
            spp_czynnoscp = new_czynn,
            spp_sposobp = self.spp_sposobp 
        )
        pop.save()


class KategorieDanych(models.Model):
    ktd_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania, 
                                    null=True,
                                    related_name="ktd_czynnosc_p",
                                    on_delete=models.CASCADE)
    
    ktd_dane = models.ForeignKey(KategoriaDanych, 
                                null=True,
                                related_name="ktd_dane_p",
                                on_delete=models.CASCADE)
   
    def clone(self, new_czynn):
        ktda = KategorieDanych(
            ktd_czynnoscp = new_czynn,
            ktd_dane = self.ktd_dane 
        )
        ktda.save()

class KategorieOsob(models.Model):
    kos_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania, 
                                    null=True,
                                    related_name="kos_czynnosc_p",
                                    on_delete=models.CASCADE)
    
    kos_kosoby = models.ForeignKey(KategoriaOsob, 
                                    null=True,
                                    related_name="kos_kosoby_p",
                                    on_delete=models.CASCADE)
   
    def clone(self, new_czynn):
        kos = KategorieOsob(
            kos_czynnoscp = new_czynn,
            kos_kosoby = self.kos_kosoby 
        )
        kos.save()

class KategorieOdbiorcow(models.Model):
    kob_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania, 
                                    null=True,
                                    related_name="kob_czynnosc_p",
                                    on_delete=models.CASCADE)
    
    kob_odbiorcy = models.ForeignKey(KategoriaOdbiorcow, 
                                    null=True,
                                    related_name="kob_odbiorcy_p",
                                    on_delete=models.CASCADE)
   
    def clone(self, new_czynn):
        ktda = KategorieOdbiorcow(
            kob_czynnoscp = new_czynn,
            kob_odbiorcy = self.kob_odbiorcy 
        )
        ktda.save()

class WysokieRyzyka(models.Model):
    wrr_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania,
                                    null=True,
                                    related_name="wrr_czynnosc_p",
                                    on_delete=models.CASCADE)
    
    wrr_wryzyka = models.ForeignKey(WysokieRyzyko, 
                                    null=True, 
                                    related_name="wrr_wryzyka_p",
                                    on_delete=models.CASCADE)
   
    def clone(self, new_czynn):
        ktda = WysokieRyzyka(
            wrr_czynnoscp = new_czynn,
            wrr_wryzyka = self.wrr_wryzyka 
        )
        ktda.save()

class PrzeslankiLegalnosci(models.Model):
    ppl_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania, 
                                    null=True, 
                                    related_name="ppl_czynnosc_p",
                                    on_delete=models.CASCADE)
    
    ppl_przeslankap = models.ForeignKey(PrzeslankaLegalnosci, 
                                    null=True, 
                                    related_name="ppl_przeslanka_p",
                                    on_delete=models.CASCADE)
   
    def clone(self, new_czynn):
        ppla = PrzeslankiLegalnosci(
            ppl_czynnoscp = new_czynn,
            ppl_przeslankap = self.ppl_przeslankap 
        )
        ppla.save()

class OperacjePrzetwarzania(models.Model):
    opp_czynnoscp = models.ForeignKey(CzynnoscPrzetwarzania, 
                                    null=True, 
                                    related_name="opp_czynnosc_p",
                                    on_delete=models.CASCADE)
    
    opp_operacjap = models.ForeignKey(OperacjaPrzetwarzania, 
                                    null=True, 
                                    related_name="opp_operacjap_p",
                                    on_delete=models.CASCADE)
   
    def clone(self, new_czynn):
        oppl = PrzeslankiLegalnosci(
            opp_czynnoscp = new_czynn,
            opp_operacjap = self.opp_operacjap 
        )
        oppl.save()

class GrupaZabezpieczen(models.Model):
    gzb_active = models.BooleanField(default=True)
    gzb_opis = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(f'{self.gzb_opis}')

    def get_absolute_url(self):
        return reverse("GrupaZabezpieczen_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("GrupaZabezpieczen_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("GrupaZabezpieczen_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("GrupaZabezpieczen_htmx_delete", args=(self.pk,))


class GrupaZagrozen(models.Model):
    gzg_active = models.BooleanField(default=True)
    gzg_opis = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(f'{self.gzg_opis}')

    def get_absolute_url(self):
        return reverse("GrupaZagrozen_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("GrupaZagrozen_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("GrupaZagrozen_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("GrupaZagrozen_htmx_delete", args=(self.pk,))


class Zagrozenie(models.Model):
    zag_active = models.BooleanField(default=True)
    zag_skrot = models.CharField(max_length=30)
    zag_opis = models.CharField(max_length=300)
    GrupaZagrozen = models.ForeignKey(GrupaZagrozen, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(f'{self.zag_skrot} - {self.zag_opis} : ({self.GrupaZagrozen})')

    def get_absolute_url(self):
        return reverse("Zagrozenie_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Zagrozenie_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Zagrozenie_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Zagrozenie_htmx_delete", args=(self.pk,))


class Zabezpieczenie(models.Model):
    zab_active = models.BooleanField(null=True, default=True)
    zab_skrot = models.CharField(null=False,max_length=30)
    zab_opis = models.CharField(null=False, max_length=300)
    zab_waga = models.IntegerField(null=True)
    GrupyZabezpieczen = models.ManyToManyField(GrupaZabezpieczen)
    Odpowiedzialni = models.ManyToManyField(Organizacja)
#    Zagrozenia = models.ManyToManyField(Zagrozenie)
    komorka = models.CharField(null=True, max_length=20)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(f'{self.zab_skrot} - {self.zab_opis}')

    def get_absolute_url(self):
        return reverse("Zabezpieczenie_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Zabezpieczenie_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Zabezpieczenie_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Zabezpieczenie_htmx_delete", args=(self.pk,))


class Podatnosc(models.Model):
    pdt_active = models.BooleanField(null=True, default=True)
    pdt_skrot = models.CharField(null=False, max_length=30)
    pdt_opis = models.CharField(null=False, max_length=300)
    pdt_waga = models.IntegerField(null=False, default=0)
    Zagrozenia = models.ManyToManyField(Zagrozenie)
    
    class Meta:
        pass

    def __str__(self):
        return str(f'{self.pdt_skrot} - {self.pdt_opis}')

    def get_absolute_url(self):
        return reverse("Podatnosc_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Podatnosc_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Podatnosc_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Podatnosc_htmx_delete", args=(self.pk,))

class ZakresOddzialywania(models.Model):
#     Zagrozenie= models.on onManyToManyField(Zagrozenie)
    zao_Poufnosc = models.BooleanField(default=True)
    zao_Integralnosc = models.BooleanField(default=True)
    zao_Dostepnosc = models.BooleanField(default=True)
    zao_Rozliczalnosc = models.BooleanField(default=True)
    zao_CiagloscDzialania = models.BooleanField(default=True)
    zao_StratyWizerunkowe = models.BooleanField(default=True)
    zao_NaruszeniePrIW = models.BooleanField(default=True)
    #Ryzyko = models.ForeignKey(Ryzyko, null=True, on_delete=models.SET_NULL)
    class Meta:
        pass

    #def __str__(self):
    #    return str(f'{self.zao_skrot} - {self.pdt_opis}')

    def get_absolute_url(self):
        return reverse("ZakresOddzialywania_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("ZakresOddzialywania_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("ZakresOddzialywania_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("ZakresOddzialywania_htmx_delete", args=(self.pk,))


class Ryzyko(models.Model):
    rr_SkalaPodatnosci = models.IntegerField(null=False, default=0)
    rr_prawdopodobienstwo_bp = models.IntegerField(null=False, default=0)
    rr_prawdopodobienstwo = models.IntegerField(null=False, default=0)
    rr_odzialywanie = models.IntegerField(null=False, default=0)
    rr_ryzyko = models.IntegerField(null=False, default=0)
    rr_redukcja = models.IntegerField(null=False, default=0)
    rr_szczatkowe = models.IntegerField(null=False, default=0)
    rr_postepowanie =  models.CharField(null=False, max_length=30, default='M')
    rr_uzasadnieniePrawdopodobienstwa =  models.CharField(null=False, max_length=500)
    rr_uzasadnienieOddzialywania =  models.CharField(null=False, max_length=500)
    rr_uzasadnienieOddzialywania_atr =  models.CharField(null=False, max_length=500)
    rr_uzasadnieniePostepowania =  models.CharField(null=False, max_length=500)
    rr_analizaRyzyka = models.CharField(null=False, max_length=500)
    Zagrozenie = models.ForeignKey(Zagrozenie, null=True, on_delete=models.SET_NULL)
    Zabezpieczenia = models.ManyToManyField(Zabezpieczenie)
    ZakresOddzialywania = models.ManyToManyField(ZakresOddzialywania)

    class Meta:
        pass

    def __str__(self):
        pass
    #    return str(f'{self.zao_skrot} - {self.pdt_opis}')

    def get_absolute_url(self):
        return reverse("Ryzyko_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Ryzyko_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Ryzyko_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Ryzyko_htmx_delete", args=(self.pk,))





class iod(models.Model):
    pass
    
    
    
    
    
    
