from django_filters.views import FilterView
from django.db.models.query import QuerySet
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy
from django_xhtml2pdf.views import PdfMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from typing import Any

from . import models
from . import forms
from . import filters


class OrganizacjaListView(generic.ListView):
    model = models.Organizacja
    form_class = forms.OrganizacjaForm
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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

class PodmiotPrzetwarzajacyListView(generic.ListView):
    model = models.PodmiotPrzetwarzajacy
    form_class = forms.PodmiotPrzetwarzajacyForm
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


class PodmiotPrzetwarzajacyCreateView(generic.CreateView):
    model = models.PodmiotPrzetwarzajacy
    form_class = forms.PodmiotPrzetwarzajacyForm


class PodmiotPrzetwarzajacyDetailView(generic.DetailView):
    model = models.PodmiotPrzetwarzajacy
    form_class = forms.PodmiotPrzetwarzajacyForm
    pk_url_kwarg = "pk"


class PodmiotPrzetwarzajacyUpdateView(generic.UpdateView):
    model = models.PodmiotPrzetwarzajacy
    form_class = forms.PodmiotPrzetwarzajacyForm
    pk_url_kwarg = "pk"


class PodmiotPrzetwarzajacyDeleteView(generic.DeleteView):
    model = models.PodmiotPrzetwarzajacy
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("PodmiotPrzetwarzajacy_list")


class RejestrListView(generic.ListView):
    model = models.Rejestr
    form_class = forms.RejestrForm
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


class OkresRetencjiCreateView(generic.CreateView):
    model = models.OkresRetencji
    form_class = forms.OkresRetencjiForm


class OkresRetencjiDetailView(generic.DetailView):
    model = models.OkresRetencji
    form_class = forms.OkresRetencjiForm


class OkresRetencjiUpdateView(generic.UpdateView):
    model = models.OkresRetencji
    form_class = forms.OkresRetencjiForm
    pk_url_kwarg = "pk"

class OkresRetencjiDeleteView(generic.DeleteView):
    model = models.OkresRetencji
    success_url = reverse_lazy("OkresRetencji_list")


class CzynnoscPrzetwarzaniaListView(generic.ListView):
    model = models.CzynnoscPrzetwarzania
    queryset = model.objects.all()
    form_class = forms.CzynnoscPrzetwarzaniaForm
    template_name = 'CzynnoscPrzetwarzaniaListView.html'
    #context_object_name = 'CzynnoscPrzetwarzania'
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = {'form' : CzynnoscPrzetwarzaniaFilterForm(), }
        # context['filter'] = CzynnoscPrzetwarzaniaFilter(self.request.GET, queryset=self.get_queryset())
        return context
      
    

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


class CzynnoscPrzetwarzaniaDeleteView(generic.DeleteView):
    model = models.CzynnoscPrzetwarzania
    success_url = reverse_lazy("CzynnoscPrzetwarzania_list")

class CzynnoscPrzetwarzaniaRODOUpdateView(generic.UpdateView):
    model = models.CzynnoscPrzetwarzania
    form_class = forms.CzynnoscPrzetwarzaniaForm
    pk_url_kwarg = "pk"

    
class CzynnoscPrzetwarzaniaRODOCreateView(generic.CreateView):
    model = models.CzynnoscPrzetwarzania
    form_class = forms.CzynnoscPrzetwarzaniaForm

# class CzynnoscPrzetwarzaniaFilterView(FilterView):
#     model = models.CzynnoscPrzetwarzania
#     context_object_name = 'czynnosci'
#     filter_class = forms.CzynnoscPrzetwarzaniaFilterForm

class CzynnoscPrzetwarzaniaRODOFilterView(FilterView):
    model = models.CzynnoscPrzetwarzania
    #context_object_name = 'CzynnoscPrzetwarzania'
    filterset_class = filters.CzynnoscPrzetwarzaniaFilter
    #paginate_by = 10

class CzynnoscPrzetwarzaniaRODOListView(generic.ListView):
    model = models.CzynnoscPrzetwarzania
    #queryset = model.objects.all()
    form_class = forms.CzynnoscPrzetwarzaniaForm
    template_name = 'CzynnoscPrzetwarzaniaListView.html'
    #context_object_name = 'czynnosci'
    filterset_class=filters.CzynnoscPrzetwarzaniaFilter
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cz_filter = filters.CzynnoscPrzetwarzaniaFilter(self.request.GET, queryset=self.queryset.all())
        context['form'] = forms.CzynnoscPrzetwarzaniaFilterForm()
        context['filter'] = cz_filter
        context['object_list'] = cz_filter.qs
        return context
    
    def get_queryset(self):
        self.queryset = super().get_queryset()
        self.filterset = filters.CzynnoscPrzetwarzaniaFilter(data=self.request.GET, queryset=self.queryset)
        return self.filterset.qs
    

class CzynnoscPrzetwarzaniaRODODetailView(generic.DetailView):
    model = models.CzynnoscPrzetwarzania
    form_class = forms.CzynnoscPrzetwarzaniaForm
    
class CzynnoscPrzetwarzaniaRODODeleteView(generic.DeleteView):
    model = models.CzynnoscPrzetwarzania
    success_url = reverse_lazy("CzynnoscPrzetwarzania_list")


class KomorkaListView(generic.ListView):
    model = models.Komorka
    form_class = forms.KomorkaForm
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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


class OperacjaPrzetwarzaniaListView(generic.ListView):
    model = models.OperacjaPrzetwarzania
    form_class = forms.OperacjaPrzetwarzaniaForm


class OperacjaPrzetwarzaniaCreateView(generic.CreateView):
    model = models.OperacjaPrzetwarzania
    form_class = forms.OperacjaPrzetwarzaniaForm


class OperacjaPrzetwarzaniaDetailView(generic.DetailView):
    model = models.OperacjaPrzetwarzania
    form_class = forms.OperacjaPrzetwarzaniaForm


class OperacjaPrzetwarzaniaUpdateView(generic.UpdateView):
    model = models.OperacjaPrzetwarzania
    form_class = forms.OperacjaPrzetwarzaniaForm
    pk_url_kwarg = "pk"


class OperacjaPrzetwarzaniaDeleteView(generic.DeleteView):
    model = models.OperacjaPrzetwarzania
    success_url = reverse_lazy("OperacjaPrzetwarzania_list")


class SposobPrzetwarzaniaListView(generic.ListView):
    model = models.SposobPrzetwarzania
    form_class = forms.SposobPrzetwarzaniaForm
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 6


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
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 6 #paginacja
    

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
    
    # def get_success_url(self):
    #     res = reverse(self.request)
    #     page_number = self.request.GET #['page']
    #     return f'{reverse(self.request.current_app)}?page={{page_number}}'

class ZabezpieczenieDeleteView(generic.DeleteView):
    model = models.Zabezpieczenie
    success_url = reverse_lazy("Zabezpieczenie_list")


class ZagrozenieListView(generic.ListView):
    model = models.Zagrozenie
    form_class = forms.ZagrozenieForm
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


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


class RyzykoListView(generic.ListView):
    model = models.Ryzyko
    form_class = forms.RyzykoForm
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    paginate_by = 10


class RyzykoCreateView(generic.CreateView):
    model = models.Ryzyko
    form_class = forms.RyzykoForm


class RyzykoDetailView(generic.DetailView):
    model = models.Ryzyko
    form_class = forms.RyzykoForm


class RyzykoUpdateView(generic.UpdateView):
    model = models.Ryzyko
    form_class = forms.RyzykoForm
    pk_url_kwarg = "pk"


class RyzykoDeleteView(generic.DeleteView):
    model = models.Ryzyko
    success_url = reverse_lazy("Ryzyko_list")

