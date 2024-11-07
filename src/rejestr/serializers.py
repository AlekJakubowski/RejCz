from rest_framework import serializers

from . import models


class CzynnoscPrzetwarzaniaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CzynnoscPrzetwarzania
        fields = '__all__'

class OrganizacjaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Organizacja
        fields = '__all__' 
        
class RejestrSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rejestr
        fields = '__all__'

class KomorkaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Komorka
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profile
        fields = '__all__'

class OkresRetencjiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.OkresRetencji
        fields = '__all__'
        
class SposobPrzetwarzaniaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.SposobPrzetwarzania
        fields = '__all__'

class KategoriaOsobSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.KategoriaOsob
        fields = '__all__'

class KategoriaOdbiorcowSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.KategoriaOdbiorcow
        fields = '__all__'


class KategoriaDanychSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.KategoriaDanych
        fields = '__all__'

class WysokieRyzykoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.WysokieRyzyko
        fields = '__all__'

class PrzeslankaLegalnosciSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.PrzeslankaLegalnosci
        fields = '__all__'



