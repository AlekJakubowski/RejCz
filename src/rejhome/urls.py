from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
#from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('htmx/', views.htmx_home, name='htmx'),
    path('admin/', admin.site.urls),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/login/", auth_views.LoginView.as_view()),
    path('rejestr/', include('rejestr.urls')),
]

