from django.views import generic
from django.urls import reverse_lazy
from django_xhtml2pdf.views import PdfMixin

from . import models
from . import forms


class OrganizacjaListView(generic.ListView):
    model = models.Organizacja
    form_class = forms.OrganizacjaForm
#    pk_url_kwarg = "pk"


class OrganizacjaCreateView(generic.CreateView):
    model = models.Organizacja
    form_class = forms.OrganizacjaForm


class OrganizacjaDetailView(generic.DetailView):
    model = models.Organizacja
    form_class = forms.OrganizacjaForm
    pk_url_kwarg = "pk"

class OrganizacjaUpdateView(generic.UpdateView):
    model = models.Organizacja
    form_class = forms.OrganizacjaForm
    pk_url_kwarg = "pk"


class OrganizacjaDeleteView(generic.DeleteView):
    model = models.Organizacja
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("Organizacja_list")


class RejestrListView(generic.ListView):
    model = models.Rejestr
    form_class = forms.RejestrForm


class RejestrCreateView(generic.CreateView):
    model = models.Rejestr
    form_class = forms.RejestrForm


class RejestrDetailView(generic.DetailView):
    model = models.Rejestr
    form_class = forms.RejestrForm
    pk_url_kwarg = "pk"


class RejestrUpdateView(generic.UpdateView):
    model = models.Rejestr
    form_class = forms.RejestrForm
    pk_url_kwarg = "pk"


class RejestrDeleteView(generic.DeleteView):
    model = models.Rejestr
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("Rejestr_list")


class OkresRetencjiListView(generic.ListView):
    model = models.OkresRetencji
    form_class = forms.OkresRetencjiForm
    pk_url_kwarg = "pk"


class OkresRetencjiCreateView(generic.CreateView):
    model = models.OkresRetencji
    form_class = forms.OkresRetencjiForm


class OkresRetencjiDetailView(generic.DetailView):
    model = models.OkresRetencji
    form_class = forms.OkresRetencjiForm
    # pk_url_kwarg = "pk"
    # success_url = reverse_lazy("OkresRetencji_detail")


class OkresRetencjiUpdateView(generic.UpdateView):
    model = models.OkresRetencji
    form_class = forms.OkresRetencjiForm
    pk_url_kwarg = "pk"

class OkresRetencjiDeleteView(generic.DeleteView):
    model = models.OkresRetencji
    success_url = reverse_lazy("OkresRetencji_list")


class CzynnoscPrzetwarzaniaListView(generic.ListView):
    model = models.CzynnoscPrzetwarzania
    form_class = forms.CzynnoscPrzetwarzaniaForm


class CzynnoscPrzetwarzaniaCreateView(generic.CreateView):
    model = models.CzynnoscPrzetwarzania
    form_class = forms.CzynnoscPrzetwarzaniaForm


class CzynnoscPrzetwarzaniaDetailView(generic.DetailView):
    model = models.CzynnoscPrzetwarzania
    form_class = forms.CzynnoscPrzetwarzaniaForm

class CzynnoscPrzetwarzaniaDetailPdfView(PdfMixin, generic.DetailView):
    model = models.CzynnoscPrzetwarzania
    template_name = "rejestr/czynnoscprzetwarzania_detail.html"

class CzynnoscPrzetwarzaniaUpdateView(generic.UpdateView):
    model = models.CzynnoscPrzetwarzania
    form_class = forms.CzynnoscPrzetwarzaniaForm
    pk_url_kwarg = "pk"


# class CzynnoscPrzetwarzaniaCloneView(generic.Clone):
#     model = models.CzynnoscPrzetwarzania
#     model.pk = None
#     form_class = forms.CzynnoscPrzetwarzaniaForm
#     pk_url_kwarg = "pk"

class CzynnoscPrzetwarzaniaDeleteView(generic.DeleteView):
    model = models.CzynnoscPrzetwarzania
    success_url = reverse_lazy("CzynnoscPrzetwarzania_list")



class KomorkaListView(generic.ListView):
    model = models.Komorka
    form_class = forms.KomorkaForm


class KomorkaCreateView(generic.CreateView):
    model = models.Komorka
    form_class = forms.KomorkaForm


class KomorkaDetailView(generic.DetailView):
    model = models.Komorka
    form_class = forms.KomorkaForm


class KomorkaUpdateView(generic.UpdateView):
    model = models.Komorka
    form_class = forms.KomorkaForm
    pk_url_kwarg = "pk"


class KomorkaDeleteView(generic.DeleteView):
    model = models.Komorka
    success_url = reverse_lazy("rejestr_Komorka_list")

class PrzeslankaLegalnosciListView(generic.ListView):
    model = models.PrzeslankaLegalnosci
    form_class = forms.PrzeslankaLegalnosciForm


class PrzeslankaLegalnosciCreateView(generic.CreateView):
    model = models.PrzeslankaLegalnosci
    form_class = forms.PrzeslankaLegalnosciForm


class PrzeslankaLegalnosciDetailView(generic.DetailView):
    model = models.PrzeslankaLegalnosci
    form_class = forms.PrzeslankaLegalnosciForm


class PrzeslankaLegalnosciUpdateView(generic.UpdateView):
    model = models.PrzeslankaLegalnosci
    form_class = forms.PrzeslankaLegalnosciForm
    pk_url_kwarg = "pk"


class PrzeslankaLegalnosciDeleteView(generic.DeleteView):
    model = models.PrzeslankaLegalnosci
    success_url = reverse_lazy("PrzeslankaLegalnosci_list")
    
class SposobPrzetwarzaniaListView(generic.ListView):
    model = models.SposobPrzetwarzania
    form_class = forms.SposobPrzetwarzaniaForm


class SposobPrzetwarzaniaCreateView(generic.CreateView):
    model = models.SposobPrzetwarzania
    form_class = forms.SposobPrzetwarzaniaForm


class SposobPrzetwarzaniaDetailView(generic.DetailView):
    model = models.SposobPrzetwarzania
    form_class = forms.SposobPrzetwarzaniaForm


class SposobPrzetwarzaniaUpdateView(generic.UpdateView):
    model = models.SposobPrzetwarzania
    form_class = forms.SposobPrzetwarzaniaForm
    pk_url_kwarg = "pk"


class SposobPrzetwarzaniaDeleteView(generic.DeleteView):
    model = models.SposobPrzetwarzania
    success_url = reverse_lazy("SposobPrzetwarzania_list")

class KategoriaOsobListView(generic.ListView):
    model = models.KategoriaOsob
    form_class = forms.KategoriaOsobForm


class KategoriaOsobCreateView(generic.CreateView):
    model = models.KategoriaOsob
    form_class = forms.KategoriaOsobForm

class KategoriaOsobDetailView(generic.DetailView):
    model = models.KategoriaOsob
    form_class = forms.KategoriaOsobForm

class KategoriaOsobUpdateView(generic.UpdateView):
    model = models.KategoriaOsob
    form_class = forms.KategoriaOsobForm
    pk_url_kwarg = "pk"

class KategoriaOsobDeleteView(generic.DeleteView):
    model = models.KategoriaOsob
    success_url = reverse_lazy("KategoriaOsob_list")

class KategoriaDanychListView(generic.ListView):
    model = models.KategoriaDanych
    form_class = forms.KategoriaDanychForm


class KategoriaDanychCreateView(generic.CreateView):
    model = models.KategoriaDanych
    form_class = forms.KategoriaDanychForm

class KategoriaDanychDetailView(generic.DetailView):
    model = models.KategoriaDanych
    form_class = forms.KategoriaDanychForm

class KategoriaDanychUpdateView(generic.UpdateView):
    model = models.KategoriaDanych
    form_class = forms.KategoriaDanychForm
    pk_url_kwarg = "pk"

class KategoriaDanychDeleteView(generic.DeleteView):
    model = models.KategoriaDanych
    success_url = reverse_lazy("KategoriaDanych_list")

class KategoriaOdbiorcowListView(generic.ListView):
    model = models.KategoriaOdbiorcow
    form_class = forms.KategoriaOdbiorcowForm


class KategoriaOdbiorcowCreateView(generic.CreateView):
    model = models.KategoriaOdbiorcow
    form_class = forms.KategoriaOdbiorcowForm

class KategoriaOdbiorcowDetailView(generic.DetailView):
    model = models.KategoriaOdbiorcow
    form_class = forms.KategoriaOdbiorcowForm

class KategoriaOdbiorcowUpdateView(generic.UpdateView):
    model = models.KategoriaOdbiorcow
    form_class = forms.KategoriaOdbiorcowForm
    pk_url_kwarg = "pk"

class KategoriaOdbiorcowDeleteView(generic.DeleteView):
    model = models.KategoriaOdbiorcow
    success_url = reverse_lazy("KategoriaOdbiorcow_list")

class WysokieRyzykoListView(generic.ListView):
    model = models.WysokieRyzyko
    form_class = forms.WysokieRyzykoForm

class WysokieRyzykoCreateView(generic.CreateView):
    model = models.WysokieRyzyko
    form_class = forms.WysokieRyzykoForm

class WysokieRyzykoDetailView(generic.DetailView):
    model = models.WysokieRyzyko
    form_class = forms.WysokieRyzykoForm

class WysokieRyzykoUpdateView(generic.UpdateView):
    model = models.WysokieRyzyko
    form_class = forms.WysokieRyzykoForm
    pk_url_kwarg = "pk"

class WysokieRyzykoDeleteView(generic.DeleteView):
    model = models.WysokieRyzyko
    success_url = reverse_lazy("WysokieRyzyko_list")

class ZabezpieczenieListView(generic.ListView):
    model = models.Zabezpieczenie
    form_class = forms.ZabezpieczenieForm

class ZabezpieczenieCreateView(generic.CreateView):
    model = models.Zabezpieczenie
    form_class = forms.ZabezpieczenieForm

class ZabezpieczenieDetailView(generic.DetailView):
    model = models.Zabezpieczenie
    form_class = forms.ZabezpieczenieForm

class ZabezpieczenieUpdateView(generic.UpdateView):
    model = models.Zabezpieczenie
    form_class = forms.ZabezpieczenieForm
    pk_url_kwarg = "pk"

class ZabezpieczenieDeleteView(generic.DeleteView):
    model = models.Zabezpieczenie
    success_url = reverse_lazy("Zabezpieczenie_list")

class ZagrozenieListView(generic.ListView):
    model = models.Zagrozenie
    form_class = forms.ZagrozenieForm

class ZagrozenieCreateView(generic.CreateView):
    model = models.Zagrozenie
    form_class = forms.ZagrozenieForm

class ZagrozenieDetailView(generic.DetailView):
    model = models.Zagrozenie
    form_class = forms.ZagrozenieForm

class ZagrozenieUpdateView(generic.UpdateView):
    model = models.Zagrozenie
    form_class = forms.ZagrozenieForm
    pk_url_kwarg = "pk"

class ZagrozenieDeleteView(generic.DeleteView):
    model = models.Zagrozenie
    success_url = reverse_lazy("Zagrozenie_list")



class GrupaZabezpieczenListView(generic.ListView):
    model = models.GrupaZabezpieczen
    form_class = forms.GrupaZabezpieczenForm

class GrupaZabezpieczenCreateView(generic.CreateView):
    model = models.GrupaZabezpieczen
    form_class = forms.GrupaZabezpieczenForm

class GrupaZabezpieczenDetailView(generic.DetailView):
    model = models.GrupaZabezpieczen
    form_class = forms.GrupaZabezpieczenForm

class GrupaZabezpieczenUpdateView(generic.UpdateView):
    model = models.GrupaZabezpieczen
    form_class = forms.GrupaZabezpieczenForm
    pk_url_kwarg = "pk"

class GrupaZabezpieczenDeleteView(generic.DeleteView):
    model = models.GrupaZabezpieczen
    success_url = reverse_lazy("GrupaZabezpieczen_list")

class GrupaZagrozenListView(generic.ListView):
    model = models.GrupaZagrozen
    form_class = forms.GrupaZagrozenForm

class GrupaZagrozenCreateView(generic.CreateView):
    model = models.GrupaZagrozen
    form_class = forms.GrupaZagrozenForm

class GrupaZagrozenDetailView(generic.DetailView):
    model = models.GrupaZagrozen
    form_class = forms.GrupaZagrozenForm

class GrupaZagrozenUpdateView(generic.UpdateView):
    model = models.GrupaZagrozen
    form_class = forms.GrupaZagrozenForm
    pk_url_kwarg = "pk"

class GrupaZagrozenDeleteView(generic.DeleteView):
    model = models.GrupaZagrozen
    success_url = reverse_lazy("GrupaZagrozen_list")

class PodatnoscListView(generic.ListView):
    model = models.Podatnosc
    form_class = forms.PodatnoscForm

class PodatnoscCreateView(generic.CreateView):
    model = models.Podatnosc
    form_class = forms.PodatnoscForm

class PodatnoscDetailView(generic.DetailView):
    model = models.Podatnosc
    form_class = forms.PodatnoscForm

class PodatnoscUpdateView(generic.UpdateView):
    model = models.Podatnosc
    form_class = forms.PodatnoscForm
    pk_url_kwarg = "pk"

class PodatnoscDeleteView(generic.DeleteView):
    model = models.Podatnosc
    success_url = reverse_lazy("Podatnosc_list")
