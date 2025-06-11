from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reviews = models.DecimalField(max_digits=3, decimal_places=2)
    category = models.CharField(max_length=100)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # For logged-in users
    session_id = models.CharField(max_length=255, null=True, blank=True)  # For anonymous users
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class ShippingDetail(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    session_id = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    shipping_method = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shipping for {self.name} ({self.shipping_method})"
