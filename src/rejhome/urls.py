from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
#from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('htmx/', views.htmx_home, name='htmx'),
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path('admin/', admin.site.urls),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path("accounts/", include('django.contrib.auth.urls')),
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("logoutpage/", TemplateView.as_view(template_name='registration/logout.html'), name='logoutpage'),
    path('rejestr/', include('rejestr.urls')),
]

