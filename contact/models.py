from django.db import models

# Create your models here.
class contact(models.Model):
    full_name=models.CharField(max_length=50)
    address=models.TextField()
    age=models.IntegerField()
    phone_number=models.CharField(max_length=10)
    birth_date=models.DateField()
    email=models.EmailField()

