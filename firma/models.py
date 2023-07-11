from django.db import models
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# Create your models here.

# kategoriya

class Category(models.Model):
    title = models.CharField(max_length=90)

    def __str__(self):
        return self.title


class Unit(models.TextChoices):
    KG = "kg"
    DONA = "dona"
    LITR = "litr"


# product turi
class ProductType(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.URLField(null=True, blank=True)
    birligi = models.CharField(max_length=30, choices=Unit.choices)
    video = models.FileField(upload_to="videos/", null=True, blank=True)

    def __str__(self):
        return self.title


class Omborxona(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


