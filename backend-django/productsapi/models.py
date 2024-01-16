from django.db import models
import cloudinary.models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ClothProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(ClothProduct, on_delete=models.CASCADE, related_name='product_images')
    image = cloudinary.models.CloudinaryField('images', null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"


