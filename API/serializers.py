from rest_framework import serializers
from .models import Kurlar

class KurlarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kurlar
        # alanlar = ('alis','satis') // belirtilen kisimlari ceker.
        # alanlar = '__all__' // tum kisimlari ceker.
        fields = '__all__'