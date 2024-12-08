from django.urls import path, include
from rest_framework import routers
from django.conf import global_settings
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Organizacja", api.OrganizacjaViewSet)
router.register("Profile", api.ProfileViewSet)
router.register("Rejestr", api.RejestrViewSet)
router.register("Komorka", api.KomorkaViewSet) 
router.register("OkresRetencji", api.OkresRetencjiViewSet) 
router.register("SposobPrzetwarzania", api.SposobPrzetwarzaniaViewSet) 
router.register("KategoriaOsob", api.KategoriaOsobViewSet) 
router.register("KategoriaOdbiorcow", api.KategoriaOdbiorcowViewSet) 
router.register("KategoriaDanych", api.KategoriaDanychViewSet) 
router.register("WysokieRyzyko", api.WysokieRyzykoViewSet) 
router.register("PrzeslankaLegalnosci", api.PrzeslankaLegalnosciViewSet) 
router.register("CzynnoscPrzetwarzania", api.CzynnoscPrzetwarzaniaViewSet, basename='WszystkieCzynnosciPrzetwarzania')
router.register("CzynnoscPrzetwarzaniaRODO", api.CzynnoscPrzetwarzaniaRODOViewSet, basename='CzynnoscPrzetwarzaniaRODO')
router.register("KategoriaCzynnosciPrzetwarzaniaRODO", api.KategoriaCzynnosciPrzetwarzaniaRODOViewSet, basename='KategoriaCzynnosciPrzetwarzaniaRODO')
router.register("CzynnoscPrzetwarzaniaDODO", api.CzynnoscPrzetwarzaniaDODOViewSet, basename='CzynnoscPrzetwarzaniaDODO')
router.register("KategoriaCzynnosciPrzetwarzaniaDODO", api.KategoriaCzynnosciPrzetwarzaniaDODOViewSet, basename='KategoriaCzynnosciPrzetwarzaniaDODO')

urlpatterns = (
    #path("api/v1/", include(router.urls)),
    #path("", include(router.urls)),
    
    #path('media/profile_images/', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),),
    # Czynność przetwarzania nie jest samodzielnną klasą, ponieważ cztery rejestry z niej dziedziczą
    # path("CzynnoscPrzetwarzania/", views.CzynnoscPrzetwarzaniaListView.as_view(), name="CzynnoscPrzetwarzania_list"),
    # path("CzynnoscPrzetwarzania/create/", views.CzynnoscPrzetwarzaniaCreateView.as_view(), name="CzynnoscPrzetwarzania_create"),
    # path("CzynnoscPrzetwarzania/detail/<int:pk>/", views.CzynnoscPrzetwarzaniaDetailView.as_view(), name="CzynnoscPrzetwarzania_detail"),
    # path("CzynnoscPrzetwarzania/update/<int:pk>/", views.CzynnoscPrzetwarzaniaUpdateView.as_view(), name="CzynnoscPrzetwarzania_update"),
    # path("CzynnoscPrzetwarzania/delete/<int:pk>/", views.CzynnoscPrzetwarzaniaDeleteView.as_view(), name="CzynnoscPrzetwarzania_delete"),
    # path("CzynnoscPrzetwarzania/pdfdetail/<int:pk>/", views.CzynnoscPrzetwarzaniaDetailPdfView.as_view(), name="CzynnoscPrzetwarzania_pdfdetail"),
    # path('CzynnoscPrzetwarzania/clone/<int:pk>/', views.CzynnoscPrzetwarzaniaCloneView.as_view(), name='CzynnoscPrzetwarzania_clone'),
    
    path("Profile/create/", views.ProfileCreateView.as_view(), name="ProfileView_create"),
    path("Profile/detail/<str:user>/", views.ProfileDetailView.as_view(), name="ProfileView_detail"),
    path("Profile/update/<str:user>/", views.ProfileUpdateView.as_view(), name="ProfileView_update"),

    path("CzynnoscPrzetwarzaniaDODO/", views.CzynnoscPrzetwarzaniaDODOListView.as_view(), name="CzynnoscPrzetwarzaniaDODO_list"),
    path("CzynnoscPrzetwarzaniaDODO/create/", views.CzynnoscPrzetwarzaniaDODOCreateView.as_view(), name="CzynnoscPrzetwarzaniaDODO_create"),
    path("CzynnoscPrzetwarzaniaDODO/detail/<int:pk>/", views.CzynnoscPrzetwarzaniaDODODetailView.as_view(), name="CzynnoscPrzetwarzaniaDODO_detail"),
    path("CzynnoscPrzetwarzaniaDODO/update/<int:pk>/", views.CzynnoscPrzetwarzaniaDODOUpdateView.as_view(), name="CzynnoscPrzetwarzaniaDODO_update"),
    path("CzynnoscPrzetwarzaniaDODO/delete/<int:pk>/", views.CzynnoscPrzetwarzaniaDODODeleteView.as_view(), name="CzynnoscPrzetwarzaniaDODO_delete"),
    path('CzynnoscPrzetwarzaniaDODO/clone/<int:pk>/', views.CzynnoscPrzetwarzaniaDODOCloneView.as_view(), name='CzynnoscPrzetwarzaniaDODO_clone'),
    #path("CzynnoscPrzetwarzaniaDODO/pdfdetail/<int:pk>/", views.CzynnoscPrzetwarzaniaDODODetailPdfView.as_view(), name="CzynnoscPrzetwarzania_pdfdetail"),
    
    path("KategoriaCzynnosciPrzetwarzaniaDODO/", views.KategoriaCzynnosciPrzetwarzaniaDODOListView.as_view(), name="KategoriaCzynnosciPrzetwarzaniaDODO_list"),
    path("KategoriaCzynnosciPrzetwarzaniaDODO/create/", views.KategoriaCzynnosciPrzetwarzaniaDODOCreateView.as_view(), name="KategoriaCzynnosciPrzetwarzaniaDODO_create"),
    path("KategoriaCzynnosciPrzetwarzaniaDODO/detail/<int:pk>/", views.KategoriaCzynnosciPrzetwarzaniaDODODetailView.as_view(), name="KategoriaCzynnosciPrzetwarzaniaDODO_detail"),
    path("KategoriaCzynnosciPrzetwarzaniaDODO/update/<int:pk>/", views.KategoriaCzynnosciPrzetwarzaniaDODOUpdateView.as_view(), name="KategoriaCzynnosciPrzetwarzaniaDODO_update"),
    path("KategoriaCzynnosciPrzetwarzaniaDODO/delete/<int:pk>/", views.KategoriaCzynnosciPrzetwarzaniaDODODeleteView.as_view(), name="KategoriaCzynnosciPrzetwarzaniaDODO_delete"),
    path('KategoriaCzynnosciPrzetwarzaniaDODO/clone/<int:pk>/', views.KategoriaCzynnosciPrzetwarzaniaDODOCloneView.as_view(), name='KategoriaCzynnosciPrzetwarzaniaDODO_clone'),
    #path("KategoriaCzynnosciPrzetwarzaniaDODO/pdfdetail/<int:pk>/", views.KategoriaCzynnosciPrzetwarzaniaDODODetailPdfView.as_view(), name="KategoriaCzynnosciPrzetwarzania_pdfdetail"),

    #path("CzynnoscPrzetwarzaniaRODO/", views.CzynnoscPrzetwarzaniaRODOFilterView.as_view(), name="CzynnoscPrzetwarzania_filteredlist"),
    path("CzynnoscPrzetwarzaniaRODO/", views.CzynnoscPrzetwarzaniaRODOListView.as_view(), name="CzynnoscPrzetwarzaniaRODO_list"),
    path("CzynnoscPrzetwarzaniaRODO/create/", views.CzynnoscPrzetwarzaniaRODOCreateView.as_view(), name="CzynnoscPrzetwarzaniaRODO_create"),
    path("CzynnoscPrzetwarzaniaRODO/detail/<int:pk>/", views.CzynnoscPrzetwarzaniaRODODetailView.as_view(), name="CzynnoscPrzetwarzaniaRODO_detail"),
    path("CzynnoscPrzetwarzaniaRODO/update/<int:pk>/", views.CzynnoscPrzetwarzaniaRODOUpdateView.as_view(), name="CzynnoscPrzetwarzaniaRODO_update"),
    path("CzynnoscPrzetwarzaniaRODO/delete/<int:pk>/", views.CzynnoscPrzetwarzaniaRODODeleteView.as_view(), name="CzynnoscPrzetwarzaniaRODO_delete"),
    path('CzynnoscPrzetwarzaniaRODO/clone/<int:pk>/', views.CzynnoscPrzetwarzaniaRODOCloneView.as_view(), name='CzynnoscPrzetwarzaniaRODO_clone'),
    #path("CzynnoscPrzetwarzaniaRODO/pdfdetail/<int:pk>/", views.CzynnoscPrzetwarzaniaRODODetailPdfView.as_view(), name="CzynnoscPrzetwarzania_pdfdetail"),

    path("KategoriaCzynnosciPrzetwarzaniaRODO/", views.KategoriaCzynnosciPrzetwarzaniaRODOListView.as_view(), name="KategoriaCzynnosciPrzetwarzaniaRODO_list"),
    path("KategoriaCzynnosciPrzetwarzaniaRODO/create/", views.KategoriaCzynnosciPrzetwarzaniaRODOCreateView.as_view(), name="KategoriaCzynnosciPrzetwarzaniaRODO_create"),
    path("KategoriaCzynnosciPrzetwarzaniaRODO/detail/<int:pk>/", views.KategoriaCzynnosciPrzetwarzaniaRODODetailView.as_view(), name="KategoriaCzynnosciPrzetwarzaniaRODO_detail"),
    path("KategoriaCzynnosciPrzetwarzaniaRODO/update/<int:pk>/", views.KategoriaCzynnosciPrzetwarzaniaRODOUpdateView.as_view(), name="KategoriaCzynnosciPrzetwarzaniaRODO_update"),
    path("KategoriaCzynnosciPrzetwarzaniaRODO/delete/<int:pk>/", views.KategoriaCzynnosciPrzetwarzaniaRODODeleteView.as_view(), name="KategoriaCzynnosciPrzetwarzaniaRODO_delete"),
    path('KategoriaCzynnosciPrzetwarzaniaRODO/clone/<int:pk>/', views.KategoriaCzynnosciPrzetwarzaniaRODOCloneView.as_view(), name='KategoriaCzynnosciPrzetwarzaniaRODO_clone'),
    #path("KategoriaCzynnosciPrzetwarzaniaRODO/pdfdetail/<int:pk>/", views.KategoriaCzynnosciPrzetwarzaniaRODODetailPdfView.as_view(), name="KategoriaCzynnosciPrzetwarzania_pdfdetail"),

    path("Rejestr/", views.RejestrListView.as_view(), name="Rejestr_list"),
    path("Rejestr/create/", views.RejestrCreateView.as_view(), name="Rejestr_create"),
    path("Rejestr/detail/<int:pk>/", views.RejestrDetailView.as_view(), name="Rejestr_detail"),
    path("Rejestr/update/<int:pk>/", views.RejestrUpdateView.as_view(), name="Rejestr_update"),
    path("Rejestr/delete/<int:pk>/", views.RejestrDeleteView.as_view(), name="Rejestr_delete"),
    path("Rejestr/clone/<int:pk>/", views.RejestrCloneView.as_view(), name="Rejestr_clone"),
    
    path("OkresRetencji/", views.OkresRetencjiListView.as_view(), name="OkresRetencji_list"),
    path("OkresRetencji/create/", views.OkresRetencjiCreateView.as_view(), name="OkresRetencji_create"),
    path("OkresRetencji/detail/<int:pk>/", views.OkresRetencjiDetailView.as_view(), name="OkresRetencji_detail"),
    path("OkresRetencji/update/<int:pk>/", views.OkresRetencjiUpdateView.as_view(), name="OkresRetencji_update"),
    path("OkresRetencji/delete/<int:pk>/", views.OkresRetencjiDeleteView.as_view(), name="OkresRetencji_delete"),
    
    path("Organizacja/", views.OrganizacjaListView.as_view(), name="Organizacja_list"),
    path("Organizacja/create/", views.OrganizacjaCreateView.as_view(), name="Organizacja_create"),
    path("Organizacja/detail/<int:pk>/", views.OrganizacjaDetailView.as_view(), name="Organizacja_detail"),
    path("Organizacja/update/<int:pk>/", views.OrganizacjaUpdateView.as_view(), name="Organizacja_update"),
    path("Organizacja/delete/<int:pk>/", views.OrganizacjaDeleteView.as_view(), name="Organizacja_delete"),
    path("Organizacja/clone/<int:pk>/", views.OrganizacjaCloneView.as_view(), name="Organizacja_clone"),

    path("PodmiotPrzetwarzajacy/", views.PodmiotPrzetwarzajacyListView.as_view(), name="PodmiotPrzetwarzajacy_list"),
    path("PodmiotPrzetwarzajacy/create/", views.PodmiotPrzetwarzajacyCreateView.as_view(), name="PodmiotPrzetwarzajacy_create"),
    path("PodmiotPrzetwarzajacy/detail/<int:pk>/", views.PodmiotPrzetwarzajacyDetailView.as_view(), name="PodmiotPrzetwarzajacy_detail"),
    path("PodmiotPrzetwarzajacy/update/<int:pk>/", views.PodmiotPrzetwarzajacyUpdateView.as_view(), name="PodmiotPrzetwarzajacy_update"),
    path("PodmiotPrzetwarzajacy/delete/<int:pk>/", views.PodmiotPrzetwarzajacyDeleteView.as_view(), name="PodmiotPrzetwarzajacy_delete"),
    
    path("Komorka/", views.KomorkaListView.as_view(), name="Komorka_list"),
    path("Komorka/create/", views.KomorkaCreateView.as_view(), name="Komorka_create"),
    path("Komorka/detail/<int:pk>/", views.KomorkaDetailView.as_view(), name="Komorka_detail"),
    path("Komorka/update/<int:pk>/", views.KomorkaUpdateView.as_view(), name="Komorka_update"),
    path("Komorka/delete/<int:pk>/", views.KomorkaDeleteView.as_view(), name="Komorka_delete"),
    path("Komorka/clone/<int:pk>/", views.KomorkaCloneView.as_view(), name="Komorka_clone"),
    
    path("PrzeslankaLegalnosci/", views.PrzeslankaLegalnosciListView.as_view(), name="PrzeslankaLegalnosci_list"),
    path("PrzeslankaLegalnosci/create/", views.PrzeslankaLegalnosciCreateView.as_view(), name="PrzeslankaLegalnosci_create"),
    path("PrzeslankaLegalnosci/detail/<int:pk>/", views.PrzeslankaLegalnosciDetailView.as_view(), name="PrzeslankaLegalnosci_detail"),
    path("PrzeslankaLegalnosci/update/<int:pk>/", views.PrzeslankaLegalnosciUpdateView.as_view(), name="PrzeslankaLegalnosci_update"),
    path("PrzeslankaLegalnosci/delete/<int:pk>/", views.PrzeslankaLegalnosciDeleteView.as_view(), name="PrzeslankaLegalnosci_delete"),

    path("OperacjaPrzetwarzania/", views.OperacjaPrzetwarzaniaListView.as_view(), name="OperacjaPrzetwarzania_list"),
    path("OperacjaPrzetwarzania/create/", views.OperacjaPrzetwarzaniaCreateView.as_view(), name="OperacjaPrzetwarzania_create"),
    path("OperacjaPrzetwarzania/detail/<int:pk>/", views.OperacjaPrzetwarzaniaDetailView.as_view(), name="OperacjaPrzetwarzania_detail"),
    path("OperacjaPrzetwarzania/update/<int:pk>/", views.OperacjaPrzetwarzaniaUpdateView.as_view(), name="OperacjaPrzetwarzania_update"),
    path("OperacjaPrzetwarzania/delete/<int:pk>/", views.OperacjaPrzetwarzaniaDeleteView.as_view(), name="OperacjaPrzetwarzania_delete"),

    path("SposobPrzetwarzania/", views.SposobPrzetwarzaniaListView.as_view(), name="SposobPrzetwarzania_list"),
    path("SposobPrzetwarzania/create/", views.SposobPrzetwarzaniaCreateView.as_view(), name="SposobPrzetwarzania_create"),
    path("SposobPrzetwarzania/detail/<int:pk>/", views.SposobPrzetwarzaniaDetailView.as_view(), name="SposobPrzetwarzania_detail"),
    path("SposobPrzetwarzania/update/<int:pk>/", views.SposobPrzetwarzaniaUpdateView.as_view(), name="SposobPrzetwarzania_update"),
    path("SposobPrzetwarzania/delete/<int:pk>/", views.SposobPrzetwarzaniaDeleteView.as_view(), name="SposobPrzetwarzania_delete"),
    path("SposobPrzetwarzania/clone/<int:pk>/", views.SposobPrzetwarzaniaCloneView.as_view(), name="SposobPrzetwarzania_clone"),

    path("KategoriaOsob/", views.KategoriaOsobListView.as_view(), name="KategoriaOsob_list"),
    path("KategoriaOsob/create/", views.KategoriaOsobCreateView.as_view(), name="KategoriaOsob_create"),
    path("KategoriaOsob/detail/<int:pk>/", views.KategoriaOsobDetailView.as_view(), name="KategoriaOsob_detail"),
    path("KategoriaOsob/update/<int:pk>/", views.KategoriaOsobUpdateView.as_view(), name="KategoriaOsob_update"),
    path("KategoriaOsob/delete/<int:pk>/", views.KategoriaOsobDeleteView.as_view(), name="KategoriaOsob_delete"),
    path('KategoriaOsob/clone/<int:pk>/', views.KategoriaOsobCloneView.as_view(), name='KategoriaOsob_clone'),

    path("KategoriaOdbiorcow/", views.KategoriaOdbiorcowListView.as_view(), name="KategoriaOdbiorcow_list"),
    path("KategoriaOdbiorcow/create/", views.KategoriaOdbiorcowCreateView.as_view(), name="KategoriaOdbiorcow_create"),
    path("KategoriaOdbiorcow/detail/<int:pk>/", views.KategoriaOdbiorcowDetailView.as_view(), name="KategoriaOdbiorcow_detail"),
    path("KategoriaOdbiorcow/update/<int:pk>/", views.KategoriaOdbiorcowUpdateView.as_view(), name="KategoriaOdbiorcow_update"),
    path("KategoriaOdbiorcow/delete/<int:pk>/", views.KategoriaOdbiorcowDeleteView.as_view(), name="KategoriaOdbiorcow_delete"),

    path("KategoriaDanych/", views.KategoriaDanychListView.as_view(), name="KategoriaDanych_list"),
    path("KategoriaDanych/create/", views.KategoriaDanychCreateView.as_view(), name="KategoriaDanych_create"),
    path("KategoriaDanych/detail/<int:pk>/", views.KategoriaDanychDetailView.as_view(), name="KategoriaDanych_detail"),
    path("KategoriaDanych/update/<int:pk>/", views.KategoriaDanychUpdateView.as_view(), name="KategoriaDanych_update"),
    path("KategoriaDanych/delete/<int:pk>/", views.KategoriaDanychDeleteView.as_view(), name="KategoriaDanych_delete"),
    path('KategoriaDanych/clone/<int:pk>/', views.KategoriaDanychCloneView.as_view(), name='KategoriaDanych_clone'),

    path("DanaWrazliwa/", views.DanaWrazliwaListView.as_view(), name="DanaWrazliwa_list"),
    path("DanaWrazliwa/create/", views.DanaWrazliwaCreateView.as_view(), name="DanaWrazliwa_create"),
    path("DanaWrazliwa/detail/<int:pk>/", views.DanaWrazliwaDetailView.as_view(), name="DanaWrazliwa_detail"),
    path("DanaWrazliwa/update/<int:pk>/", views.DanaWrazliwaUpdateView.as_view(), name="DanaWrazliwa_update"),
    path("DanaWrazliwa/delete/<int:pk>/", views.DanaWrazliwaDeleteView.as_view(), name="DanaWrazliwa_delete"),
    path('DanaWrazliwa/clone/<int:pk>/', views.DanaWrazliwaCloneView.as_view(), name='DanaWrazliwa_clone'),

    path("WysokieRyzyko/", views.WysokieRyzykoListView.as_view(), name="WysokieRyzyko_list"),
    path("WysokieRyzyko/create/", views.WysokieRyzykoCreateView.as_view(), name="WysokieRyzyko_create"),
    path("WysokieRyzyko/detail/<int:pk>/", views.WysokieRyzykoDetailView.as_view(), name="WysokieRyzyko_detail"),
    path("WysokieRyzyko/update/<int:pk>/", views.WysokieRyzykoUpdateView.as_view(), name="WysokieRyzyko_update"),
    path("WysokieRyzyko/delete/<int:pk>/", views.WysokieRyzykoDeleteView.as_view(), name="WysokieRyzyko_delete"),

    path("Zagrozenie/", views.ZagrozenieListView.as_view(), name="Zagrozenie_list"),
    path("Zagrozenie/create/", views.ZagrozenieCreateView.as_view(), name="Zagrozenie_create"),
    path("Zagrozenie/detail/<int:pk>/", views.ZagrozenieDetailView.as_view(), name="Zagrozenie_detail"),
    path("Zagrozenie/update/<int:pk>/", views.ZagrozenieUpdateView.as_view(), name="Zagrozenie_update"),
    path("Zagrozenie/delete/<int:pk>/", views.ZagrozenieDeleteView.as_view(), name="Zagrozenie_delete"),

    path("Podatnosc/", views.PodatnoscListView.as_view(), name="Podatnosc_list"),
    path("Podatnosc/create/", views.PodatnoscCreateView.as_view(), name="Podatnosc_create"),
    path("Podatnosc/detail/<int:pk>/", views.PodatnoscDetailView.as_view(), name="Podatnosc_detail"),
    path("Podatnosc/update/<int:pk>/", views.PodatnoscUpdateView.as_view(), name="Podatnosc_update"),
    path("Podatnosc/delete/<int:pk>/", views.PodatnoscDeleteView.as_view(), name="Podatnosc_delete"),

    path("Zabezpieczenie/", views.ZabezpieczenieListView.as_view(), name="Zabezpieczenie_list"),
    path("Zabezpieczenie/create/", views.ZabezpieczenieCreateView.as_view(), name="Zabezpieczenie_create"),
    path("Zabezpieczenie/detail/<int:pk>/", views.ZabezpieczenieDetailView.as_view(), name="Zabezpieczenie_detail"),
    path("Zabezpieczenie/update/<int:pk>/", views.ZabezpieczenieUpdateView.as_view(), name="Zabezpieczenie_update"),
    path("Zabezpieczenie/delete/<int:pk>/", views.ZabezpieczenieDeleteView.as_view(), name="Zabezpieczenie_delete"),
    
    path("GrupaZagrozen/", views.GrupaZagrozenListView.as_view(), name="GrupaZagrozen_list"),
    path("GrupaZagrozen/create/", views.GrupaZagrozenCreateView.as_view(), name="GrupaZagrozen_create"),
    path("GrupaZagrozen/detail/<int:pk>/", views.GrupaZagrozenDetailView.as_view(), name="GrupaZagrozen_detail"),
    path("GrupaZagrozen/update/<int:pk>/", views.GrupaZagrozenUpdateView.as_view(), name="GrupaZagrozen_update"),
    path("GrupaZagrozen/delete/<int:pk>/", views.GrupaZagrozenDeleteView.as_view(), name="GrupaZagrozen_delete"),

    path("GrupaZabezpieczen/", views.GrupaZabezpieczenListView.as_view(), name="GrupaZabezpieczen_list"),
    path("GrupaZabezpieczen/create/", views.GrupaZabezpieczenCreateView.as_view(), name="GrupaZabezpieczen_create"),
    path("GrupaZabezpieczen/detail/<int:pk>/", views.GrupaZabezpieczenDetailView.as_view(), name="GrupaZabezpieczen_detail"),
    path("GrupaZabezpieczen/update/<int:pk>/", views.GrupaZabezpieczenUpdateView.as_view(), name="GrupaZabezpieczen_update"),
    path("GrupaZabezpieczen/delete/<int:pk>/", views.GrupaZabezpieczenDeleteView.as_view(), name="GrupaZabezpieczen_delete"),

    # path("htmx/Organizacja/", htmx.HTMXOrganizacjaListView.as_view(), name="Organizacja_htmx_list"),
    # path("htmx/Organizacja/create/", htmx.HTMXOrganizacjaCreateView.as_view(), name="Organizacja_htmx_create"),
    # path("htmx/Organizacja/delete/<int:pk>/", htmx.HTMXOrganizacjaDeleteView.as_view(), name="Organizacja_htmx_delete"),
    
    # path("htmx/CzynnoscPrzetwarzania/", htmx.HTMXCzynnoscPrzetwarzaniaListView.as_view(), name="CzynnoscPrzetwarzania_htmx_list"),
    # path("htmx/CzynnoscPrzetwarzania/create/", htmx.HTMXCzynnoscPrzetwarzaniaCreateView.as_view(), name="CzynnoscPrzetwarzania_htmx_create"),
    # path("htmx/CzynnoscPrzetwarzania/delete/<int:pk>/", htmx.HTMXCzynnoscPrzetwarzaniaDeleteView.as_view(), name="CzynnoscPrzetwarzania_htmx_delete"),
    
    # path("htmx/Rejestr/", htmx.HTMXRejestrListView.as_view(), name="htmx_list"),
    # path("htmx/Rejestr/create/", htmx.HTMXRejestrCreateView.as_view(), name="htmx_create"),
    # path("htmx/Rejestr/delete/<int:pk>/", htmx.HTMXRejestrDeleteView.as_view(), name="htmx_delete"),
    
    # path("htmx/Komorka/", htmx.HTMXKomorkaListView.as_view(), name="Komorka_htmx_list"),
    # path("htmx/Komorka/create/", htmx.HTMXKomorkaCreateView.as_view(), name="Komorka_htmx_create"),
    # path("htmx/Komorka/delete/<int:pk>/", htmx.HTMXKomorkaDeleteView.as_view(), name="Komorka_htmx_delete"),
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
)

# if settings.DEBUG: 
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)