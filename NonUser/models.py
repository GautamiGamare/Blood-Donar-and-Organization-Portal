from django.db import models

class Nonuser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cno = models.IntegerField()
    msg = models.CharField(max_length=100)
    status = models.CharField(max_length=20,default="Pending")

