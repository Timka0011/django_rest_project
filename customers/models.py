from django.db import models

# Create your models here.


class Buyurtmachi(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    address = models.TextField()
    firma_nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.firma_nomi




