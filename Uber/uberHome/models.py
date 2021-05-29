from django.db import models

# Create your models here.
class Servicing(models.Model):
    name=models.CharField(max_length=100)
    Vehicle_number=models.IntegerField()
    Owner_Name =models.CharField(max_length=100)
    Service_Requested=models.CharField(max_length=100)
    price=models.IntegerField()
    paid=models.BooleanField()



