from django.db import models

class Companyy(models.Model):
    name = models.CharField(null=True, max_length=30)
    symbol = models.CharField(max_length=5, primary_key=True, default=0)  
    ESG = models.IntegerField(null=True)
    EV = models.IntegerField(null=True)
    NH = models.IntegerField(null=True)
    CT = models.IntegerField(null=True)
    FS = models.IntegerField(null=True)





# Create your models here.
