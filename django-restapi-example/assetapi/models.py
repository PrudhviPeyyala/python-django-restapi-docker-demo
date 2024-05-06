from django.db import models


# Create your models here.
class Asset(models.Model):
    assetType = models.CharField(max_length=50)
    assetManufacturer = models.CharField(max_length=50)
    assetModel = models.CharField(max_length=50)
