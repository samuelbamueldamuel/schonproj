from django.db import models

class Company(models.Model):
    name = models.CharField(null=False),
    symbol = models.CharField(max_length=5, primary_key=5),

class Sustainability(models.Model):
    symbol = models.OneToOneField(Company, related_name='susSymbol', on_delete=models.CASCADE)
    ESG = models.IntegerField()
    carbon = models.IntegerField()

class Stock(models.Model):
    symbol = models.ForeignKey(Company, related_name='stockSymbol', on_delete=models.CASCADE)
    date = models.CharField(max_length=10)
    price = models.IntegerField()
    volume = models.IntegerField()



# Create your models here.
