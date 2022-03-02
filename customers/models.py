from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="customers/logos", default="no_picture.png")

    def __str__(self):
        return str(self.name)


    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)