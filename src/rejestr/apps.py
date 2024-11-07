from django.apps import AppConfig
#from django.db.models import *

class RejestrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rejestr'

    # funkcja potrzebna do 
    # sygnałów/triggerów zapisu lub utworzenia 
    # nowych rekordów np; profilu usera
    def ready(self):
        import django.db.models.signals