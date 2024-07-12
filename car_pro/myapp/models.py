from django.db import models

class CarManufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SparePart(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
