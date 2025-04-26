from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import PozycjaRejestru, Komorka
from django.contrib.auth.models import User

from django.test import TestCase
from .models import PozycjaRejestru

class PozycjaRejestruTestCase(TestCase):
    def test_create_pozycja(self):
        komorka = "2001-IWD"
        pozycja = PozycjaRejestru.objects.create(
            pzr_pozycja_rej=1,
            pzr_prefix_komorki=komorka,
            pzr_status_zatw='OCZEKUJĄCA',
        )
        self.assertEqual(pozycja.pzr_prefix_komorki, komorka)
        
class PozycjaRejestruViewTest(TestCase):
    def test_filtrowanie_po_komorce(self):
        user = User.objects.create(username="testuser")
        komorka = Komorka.objects.create(prefix="2001-IWD")
        profile = user.profile
        profile.pro_komorka = komorka
        profile.save()
        PozycjaRejestru.objects.create(pzr_prefix_komorki="2001-IWD", pzr_pozycja_rej=1)
        PozycjaRejestru.objects.create(pzr_prefix_komorki="2002-XYZ", pzr_pozycja_rej=2)

        self.client.force_login(user)
        response = self.client.get('/list/')
        self.assertContains(response, "2001-IWD")
        self.assertNotContains(response, "2002-XYZ")