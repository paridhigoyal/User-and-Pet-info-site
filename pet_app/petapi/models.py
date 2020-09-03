from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pet(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length = 40)
    category = models.CharField(max_length = 40)
    color = models.CharField(max_length = 20)
    birth_date = models.DateField() 

    def __str__(self):
        return self.name
