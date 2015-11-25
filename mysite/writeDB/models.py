from django.db import models

# Create your models here.
class ngo(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    person = models.CharField(max_length=100, blank=True)
    purpose = models.TextField(max_length=500, blank=True)
    aim = models.TextField(max_length=500, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

class address_map(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

