from django.db import models
from django.contrib.auth.models import User


class CarBrand(models.Model):
    name=models.CharField(max_length=150)
    country=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Car(models.Model):
    model_name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    color=models.TextField()
    year=models.DateField()
    brand=models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.model_name

class Comment(models.Model):
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text

