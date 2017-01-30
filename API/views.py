from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Kurlar
from .serializers import KurlarSerializer

# Create your views here.

class KurListesi(APIView):

    def get(self, request):
        kurlar = Kurlar.objects.all()
        serializer = KurlarSerializer(kurlar, many=True)
        return  Response(serializer.data)

    def post(self):
        pass