# This class defines a Django model for student data with fields for ID, name, age, email, password,
# and address.
from django.db import models

# Create your models here.
class Stu_Data(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
    address = models.CharField(max_length=70,default='')