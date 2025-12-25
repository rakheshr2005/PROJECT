from django.db import models


# Create your models here.

class user_details(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    dob=models.DateField()
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=40)

    def __str__(self):
        return self.firstname

