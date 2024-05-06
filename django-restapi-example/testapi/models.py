from django.db import models


# Create your models here.
class Bike(models.Model):
    modelName = models.CharField(max_length=50)
    manufacturer = models.TextField()
    activeOrNot = models.BooleanField()

    def __str__(self):
        return self.modelName
