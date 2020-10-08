from django.db import models
from Donar.models import DonarModel
from Organization.models import OrganizationModel

class adminModel(models.Model):
    id = models.AutoField(primary_key= True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class chatInfo(models.Model):
    id =models.AutoField(primary_key=True)
    sender_name = models.CharField(max_length=20)
    sender = models.CharField(max_length=20)
    receiver_name = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    message = models.CharField(max_length=500)
    status = models.CharField(max_length=20,default="Pending")

