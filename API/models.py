from django.db import models

# Modeller burada tanimlanacak.

class Kurlar (models.Model):
    #Doviz ismi DOLAR/TL
    doviz_ismi = models.CharField(max_length=10)
    alis = models.FloatField() #alis fiyati
    satis = models.FloatField() #satis fiyati
    fark = models.FloatField() #fark
    kur_kodu = models.CharField(max_length=10) #USD/TL

    def __str__(self):
        return self.doviz_ismi