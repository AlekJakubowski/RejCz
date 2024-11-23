from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.contrib import messages
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy

class RegisterView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    
class LoginView(LoginView):
    form_class = AuthenticationForm
    #redirect_authenticated_user = True # po wylogowaniu będzie problemz przekierowaniem
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')
        
    def get_success_url(self):
        if not hasattr(self.request.user, 'profile'):
            return reverse('ProfileView_create')  # Nazwa ścieżki do `ProfileCreateView`
        return super().get_success_url()
    
class LogoutView(LogoutView):
    template_name = 'users/logout.html'
    success_url = reverse_lazy('login')
