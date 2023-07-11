from django.db import models
from firma.models import Product_Type
from customers.models import Buyurtmachi
# Create your models here.


class Product(models.Model):
    product_type = models.ForeignKey(Product_Type, on_delete=models.CASCADE, related_name="product_type")
    customer = models.ForeignKey(Buyurtmachi, on_delete=models.CASCADE)
    narx_1 = models.CharField(max_length=150)
    narx_2 = models.CharField(max_length=150)

    def __str__(self):
        return self.product_type


class PurchasedProduct(models.Model):
    product = models.ManyToManyField(Product, related_name="product")
    customer = models.ForeignKey(Buyurtmachi, on_delete=models.CASCADE, related_name="customer")
    time_taken = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    is_sale = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product


class ProductInStock(models.Model):
    product = models.ForeignKey(Product, )
