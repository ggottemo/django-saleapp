from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products", default="no_picture.png")
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="USD")
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}-${self.price}-{self.stock}-{self.created_at.strftime('%d/%m/%Y')}"