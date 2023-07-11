from django.db import models


# Create your models here.

# kategoriya

class Category(models.Model):
    title = models.CharField(max_length=90)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Unit(models.TextChoices):
    KG = "kg"
    DONA = "dona"
    LITR = "litr"


# product turi

class Product_Type(models.Model):
    title = models.CharField(max_length=150)
    image = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    birligi = models.CharField(max_length=30, choices=Unit.choices)
    video = models.FileField(upload_to="videos/", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product_Turi"
        verbose_name_plural = "Product_Turlari"


class Omborxona(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Omborxona"
        verbose_name_plural = "Omborxonalar"

