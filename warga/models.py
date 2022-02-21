from django.db import models

# Create your models here.
class Warga(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    address = models.TextField()
