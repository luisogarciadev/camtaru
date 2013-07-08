from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)


class Route(models.Model):
    active = models.BooleanField()
    vehicle = models.ForeignKey('Vehicle')
