from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
#from django.contrib.auth.decorators import login_required, method_decorator
from django.contrib import messages
from django.contrib.auth import  authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import  User
from django.contrib import auth
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy
#from django.forms import form
from django.shortcuts import get_object_or_404, redirect
from django_filters.views import FilterView
from django_xhtml2pdf.views import PdfMixin
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
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
    
class OrganizacjaCloneView(generic.View):
    model = models.Organizacja

    def post(self, request, pk):
        # Pobierz obiekt do sklonowania
        instance = get_object_or_404(models.Organizacja, pk=pk)

        # Klonowanie obiektu
        instance.clone(instance)
    
        # Przekierowanie z powrotem do listy obiektów lub innej strony
        return redirect('Organizacja_list')


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

class ProfileDeleteView(generic.DeleteView):
    model = models.Profile
    success_url = reverse_lazy("login")
    pk_url_kwarg = "pk"

class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
    #model = models.Profile
    form_class = forms.ProfileForm
    template_name = "rejestr/profile_form.html"
    success_url = reverse_lazy('index')  # lub inna strona po zakończeniu tworzenia profilu

    def get_initial(self):
        initial = super().get_initial()
        initial['pro_user'] = self.request.user.id  # Przekazanie nazwy użytkownika jako wartość początkową
        initial['pro_login'] = self.request.user.username  # Przekazanie nazwy użytkownika jako wartość początkową
        return initial

    def form_valid(self, form):
        # Zapisz profil i przypisz go do aktualnie zalogowanego użytkownika
        profile = form.save(commit=False)
        profile.pro_user = self.request.user
        profile.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        # Przekierowanie na widok szczegółów z użyciem pk nowo utworzonego profilu
        return reverse('ProfileView_detail', kwargs={'pk': self.object.pk})

    class meta:
        model = models.Profile
        fields = ['pro_user', 'pro_nazwa', 'pro_opis', 
                  'pro_rola','pro_organizacja', 'pro_komorka', 'pro_komorki']

# class ProfileUpdateView(generic.UpdateView):
#     model = models.Profile
#     form_class = forms.ProfileUpdateForm
#     pk_url_kwarg = "pk"


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Profile
    #template_name = 'profile_update.html'  # Define your template path
   
    fields = ['pro_user', 'pro_nazwa', 'pro_opis', 
            'pro_rola','pro_organizacja', 'pro_komorka', 'pro_komorki']

    def get_object(self, queryset=None):
        # Fetch the user by username
        username = self.kwargs.get('user')
        user = get_object_or_404(User, username=username)
        # Then, retrieve or create their profile
        profile, created = models.Profile.objects.get_or_create(pro_user=user)
        profile.pro_user = user
        
        return profile


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Profile
    fields = "__all__"
    form_class = forms.ProfileForm
    
    def get_object(self, queryset=None):
        # Fetch the user by username
        username = self.kwargs.get('user')
        user = get_object_or_404(User, username=username)
        # Then, retrieve or create their profile
        profile, created = models.Profile.objects.get_or_create(pro_user=user)
        profile.pro_user = user
        
        return profile

class ProfileImageView(generic.ListView):
    model = models.Profile
    form_class = forms.ProfileForm
    
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

class RejestrCloneView(generic.View):
    model = models.Rejestr

    def post(self, request, pk):
        # Pobierz obiekt do sklonowania
        instance = get_object_or_404(models.Rejestr, pk=pk)

        # Klonowanie obiektu
        instance.clone(instance)
    
        # Przekierowanie z powrotem do listy obiektów lub innej strony
        return redirect('Organizacja_list')

class OkresRetencjiListView(generic.ListView):
    model = models.OkresRetencji
    form_class = forms.OkresRetencjiForm
    pk_url_kwarg = "pk"
    # włączenie paginacji tabeli na n=10 wierszy
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


class CzynnoscPrzetwarzaniaDODOUpdateView(generic.UpdateView):
    model = models.CzynnoscPrzetwarzaniaDODO
    form_class = forms.CzynnoscPrzetwarzaniaDODOForm
    pk_url_kwarg = "pk"


class CzynnoscPrzetwarzaniaDODOCreateView(generic.CreateView):
    model = models.CzynnoscPrzetwarzaniaDODO
    form_class = forms.CzynnoscPrzetwarzaniaDODOForm


class CzynnoscPrzetwarzaniaDODOFilterView(FilterView):
    model = models.CzynnoscPrzetwarzaniaDODO
    #filterset_class = filters.CzynnoscPrzetwarzaniaFilter
    #paginate_by = 10


class CzynnoscPrzetwarzaniaDODOListView(generic.ListView):
    model = models.CzynnoscPrzetwarzaniaDODO
    queryset = model.objects.filter(Rejestr=3).order_by('czn_pozycja_rej')
    form_class = forms.CzynnoscPrzetwarzaniaDODOForm
    #filterset_class=filters.CzynnoscPrzetwarzaniaFilter
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    #paginate_by = 10


class CzynnoscPrzetwarzaniaDODODetailView(generic.DetailView):
    model = models.CzynnoscPrzetwarzaniaDODO
    form_class = forms.CzynnoscPrzetwarzaniaDODOForm


class CzynnoscPrzetwarzaniaDODODeleteView(generic.DeleteView):
    model = models.CzynnoscPrzetwarzaniaDODO
    success_url = reverse_lazy("CzynnoscPrzetwarzaniaDODO_list")


class CzynnoscPrzetwarzaniaDODOCloneView(generic.View):
    model = models.CzynnoscPrzetwarzaniaDODO

    def post(self, request, pk):
        # Pobierz obiekt do sklonowania
        instance = get_object_or_404(models.CzynnoscPrzetwarzaniaDODO, pk=pk)

        # Klonowanie obiektu
        instance.clone()
    
        # Przekierowanie z powrotem do listy obiektów lub innej strony
        return redirect('CzynnoscPrzetwarzaniaDODO_list')  


class KategoriaCzynnosciPrzetwarzaniaDODOUpdateView(generic.UpdateView):
    model = models.KategoriaCzynnosciPrzetwarzaniaDODO
    form_class = forms.KategoriaCzynnosciPrzetwarzaniaDODOForm
    pk_url_kwarg = "pk"


class KategoriaCzynnosciPrzetwarzaniaDODOCreateView(generic.CreateView):
    model = models.KategoriaCzynnosciPrzetwarzaniaDODO
    form_class = forms.KategoriaCzynnosciPrzetwarzaniaDODOForm


class KategoriaCzynnosciPrzetwarzaniaDODOFilterView(FilterView):
    model = models.KategoriaCzynnosciPrzetwarzaniaDODO
    #context_object_name = 'KategoriaCzynnosciPrzetwarzania'
    #filterset_class = filters.KategoriaCzynnosciPrzetwarzaniaFilter
    #paginate_by = 10

class KategoriaCzynnosciPrzetwarzaniaDODOListView(generic.ListView):
    model = models.KategoriaCzynnosciPrzetwarzaniaDODO
    queryset = model.objects.filter(Rejestr=4).order_by('czn_pozycja_rej')
    form_class = forms.KategoriaCzynnosciPrzetwarzaniaDODOForm
    #context_object_name = 'czynnosci'
    #filterset_class=filters.KategoriaCzynnosciPrzetwarzaniaFilter
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    #paginate_by = 10
        

class KategoriaCzynnosciPrzetwarzaniaDODODetailView(generic.DetailView):
    model = models.KategoriaCzynnosciPrzetwarzaniaDODO
    form_class = forms.KategoriaCzynnosciPrzetwarzaniaDODOForm
    
class KategoriaCzynnosciPrzetwarzaniaDODODeleteView(generic.DeleteView):
    model = models.KategoriaCzynnosciPrzetwarzaniaDODO
    success_url = reverse_lazy("KategoriaCzynnosciPrzetwarzaniaDODO_list")

class KategoriaCzynnosciPrzetwarzaniaDODOCloneView(generic.View):
    model = models.KategoriaCzynnosciPrzetwarzaniaDODO

    def post(self, request, pk):
        # Pobierz obiekt do sklonowania
        instance = get_object_or_404(models.KategoriaCzynnosciPrzetwarzaniaDODO, pk=pk)

        # Klonowanie obiektu
        instance.clone()
    
        # Przekierowanie z powrotem do listy obiektów lub innej strony
        return redirect('KategoriaCzynnosciPrzetwarzaniaDODO_list')  

class CzynnoscPrzetwarzaniaRODOUpdateView(generic.UpdateView):
    model = models.CzynnoscPrzetwarzaniaRODO
    form_class = forms.CzynnoscPrzetwarzaniaRODOForm
    pk_url_kwarg = "pk"
    
class CzynnoscPrzetwarzaniaRODOCreateView(generic.CreateView):
    model = models.CzynnoscPrzetwarzaniaRODO
    form_class = forms.CzynnoscPrzetwarzaniaRODOForm
    #form_class.Rejestr.initial = 1
    #pass

class CzynnoscPrzetwarzaniaRODOFilterView(FilterView):
    model = models.CzynnoscPrzetwarzaniaRODO
    filterset_class = filters.CzynnoscPrzetwarzaniaFilter
    #paginate_by = 10

class CzynnoscPrzetwarzaniaRODOListView(generic.ListView):
    model = models.CzynnoscPrzetwarzaniaRODO
    queryset = model.objects.filter(Rejestr = 1).order_by('czn_pozycja_rej')
    form_class = forms.CzynnoscPrzetwarzaniaRODOForm
    #context_object_name = 'czynnosci'
    #filterset_class=filters.CzynnoscPrzetwarzaniaFilter
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    #paginate_by = 10
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     cz_filter = filters.CzynnoscPrzetwarzaniaFilter(self.request.GET, queryset=self.queryset.all())
    #     context['form'] = forms.CzynnoscPrzetwarzaniaFilterForm()
    #     context['filter'] = cz_filter
    #     context['object_list'] = cz_filter.qs
    #     return context
    
    # def get_queryset(self):
    #     self.queryset = super().get_queryset()
    #     self.filterset = filters.CzynnoscPrzetwarzaniaFilter(data=self.request.GET, queryset=self.queryset)
    #     return self.filterset.qs

class CzynnoscPrzetwarzaniaRODODetailView(generic.DetailView):
    model = models.CzynnoscPrzetwarzaniaRODO
    form_class = forms.CzynnoscPrzetwarzaniaRODOForm
    
class CzynnoscPrzetwarzaniaRODODeleteView(generic.DeleteView):
    model = models.CzynnoscPrzetwarzaniaRODO
    success_url = reverse_lazy("CzynnoscPrzetwarzaniaRODO_list")

class CzynnoscPrzetwarzaniaRODOCloneView(generic.View):
    model = models.CzynnoscPrzetwarzania

    def post(self, request, pk):
        # Pobierz obiekt do sklonowania
        instance = get_object_or_404(models.CzynnoscPrzetwarzaniaRODO, pk=pk)

        # Klonowanie obiektu
        instance.clone()
    
        # Przekierowanie z powrotem do listy obiektów lub innej strony
        return redirect('CzynnoscPrzetwarzaniaRODO_list')  

class KategoriaCzynnosciPrzetwarzaniaRODOUpdateView(generic.UpdateView):
    model = models.KategoriaCzynnosciPrzetwarzaniaRODO
    form_class = forms.KategoriaCzynnosciPrzetwarzaniaRODOForm
    pk_url_kwarg = "pk"
    
class KategoriaCzynnosciPrzetwarzaniaRODOCreateView(generic.CreateView):
    model = models.KategoriaCzynnosciPrzetwarzaniaRODO
    form_class = forms.KategoriaCzynnosciPrzetwarzaniaRODOForm
    #template_name = 'templates/czynnoscprzetwarzaniaRODO_list.html'

class KategoriaCzynnosciPrzetwarzaniaRODOFilterView(FilterView):
    model = models.KategoriaCzynnosciPrzetwarzaniaRODO
    #context_object_name = 'KategoriaCzynnosciPrzetwarzania'
    #filterset_class = filters.KategoriaCzynnosciPrzetwarzaniaFilter
    #paginate_by = 10

class KategoriaCzynnosciPrzetwarzaniaRODOListView(generic.ListView):
    model = models.KategoriaCzynnosciPrzetwarzaniaRODO
    queryset = model.objects.filter(Rejestr=2).order_by('czn_pozycja_rej')
    form_class = forms.CzynnoscPrzetwarzaniaRODOForm
    #template_name = 'templates/czynnoscprzetwarzaniaKatRODO_list.html'
    #context_object_name = 'czynnosci'
    #filterset_class=filters.CzynnoscPrzetwarzaniaForm
    # właczenie paginacji tabeli na n=10 wierszy
    #jeśli wiersze są wyższe może być 6 lub mniej
    #paginate_by = 10
    
class KategoriaCzynnosciPrzetwarzaniaRODODetailView(generic.DetailView):
    model = models.KategoriaCzynnosciPrzetwarzaniaRODO
    form_class = forms.KategoriaCzynnosciPrzetwarzaniaRODOForm
    
class KategoriaCzynnosciPrzetwarzaniaRODODeleteView(generic.DeleteView):
    model = models.KategoriaCzynnosciPrzetwarzaniaRODO
    success_url = reverse_lazy("KategoriaCzynnosciPrzetwarzaniaRODO_list")

class KategoriaCzynnosciPrzetwarzaniaRODOCloneView(generic.View):
    model = models.KategoriaCzynnosciPrzetwarzaniaRODO

    def post(self, request, pk):
        # Pobierz obiekt do sklonowania
        instance = get_object_or_404(models.KategoriaCzynnosciPrzetwarzaniaRODO, pk=pk)

        # Klonowanie obiektu
        instance.clone()
    
        # Przekierowanie z powrotem do listy obiektów lub innej strony
        return redirect('KategoriaCzynnosciPrzetwarzaniaRODO_list')  

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

class KomorkaCloneView(generic.View):
    model = models.Rejestr

    def post(self, request, pk):
        # Pobierz obiekt do sklonowania
        instance = get_object_or_404(models.Komorka, pk=pk)

        # Klonowanie obiektu
        instance.clone(instance)
    
        # Przekierowanie z powrotem do listy obiektów lub innej strony
        return redirect('Komorka_list')


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

class SposobPrzetwarzaniaCloneView(generic.View):
    model = models.SposobPrzetwarzania

    def post(self, request, pk):
        # Pobierz obiekt do sklonowania
        instance = get_object_or_404(models.SposobPrzetwarzania, pk=pk)

        # Klonowanie obiektu
        instance.clone(instance)
    
        # Przekierowanie z powrotem do listy obiektów lub innej strony
        return redirect('SposobPrzetwarzania_list')

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
    
class KategoriaOsobCloneView(generic.View):
    model = models.KategoriaOsob

    def post(self, request, pk):
        # Pobierz obiekt do sklonowania
        instance = get_object_or_404(models.KategoriaOsob, pk=pk)

        # Klonowanie obiektu
        instance.clone(instance)
    
        # Przekierowanie z powrotem do listy obiektów lub innej strony
        return redirect('KategoriaOsob_list')
    
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

class KategoriaDanychCloneView(generic.View):
    model = models.KategoriaDanych

    def post(self, request, pk):
        # Pobierz obiekt do sklonowania
        instance = get_object_or_404(models.KategoriaDanych, pk=pk)

        # Klonowanie obiektu
        instance.clone(instance)
    
        # Przekierowanie z powrotem do listy obiektów lub innej strony
        return redirect('KategoriaDanych_list')
    
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

