from django.db import models
from passlib.hash import pbkdf2_sha256

class DonarModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact_number = models.IntegerField()
    contact_number_2 = models.IntegerField()
    email = models.EmailField(max_length=40,unique=True)
    blood_group = models.CharField(max_length=10)
    last_donation_date = models.DateField()
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="donar_images/",null=True)
    password = models.CharField(max_length=30)

    def verify_password(self,raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)