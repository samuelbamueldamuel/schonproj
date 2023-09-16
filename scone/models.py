from django.db import models

class Sustain(models.Model):
    name = models.CharField(null=False),
    symbol = models.CharField(max_length=4),
    price = models.IntegerField(),
    worth = models.IntegerField(),
    carbonFootprint = models.IntegerField(),
    carbonNeutral = models.IntegerField(),
    renewable = models.IntegerField(),
    safety = models.IntegerField(),
    vetProgram = models.IntegerField(),
    wasteManagment = models.IntegerField(),
    CSR = models.IntegerField(),
    philanthrophy = models.IntegerField(),


# Create your models here.
