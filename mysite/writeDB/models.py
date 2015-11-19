from django.db import models

# Create your models here.
class ngo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=60, blank=True)
    mobile = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    person = models.CharField(max_length=100, blank=True)
    purpose = models.CharField(max_length=200, blank=True)
    aim = models.TextField(max_length=500, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

