from django.db import models

class OrganizationModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    contact_number = models.IntegerField()
    contact_number_2 = models.IntegerField()
    email = models.EmailField(max_length=40,unique=True)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="organization_images/")
    status = models.CharField(max_length=20,default="Pending")
    uname = models.CharField(max_length=30,default="uname")
    password = models.CharField(max_length=30, default="password")
