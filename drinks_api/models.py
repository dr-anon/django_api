from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    hair_color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    