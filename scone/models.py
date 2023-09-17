from django.db import models

class Company(models.Model):
    name = models.CharField(null=False),
    symbol = models.CharField(max_length=5, primary_key=5),
    ESG = models.IntegerField(null=True)
    EV = models.IntegerField(null=True)
    NH = models.IntegerField(null=True)
    CT = models.IntegerField(null=True)
    FS = models.IntegerField(null=True)





# Create your models here.
