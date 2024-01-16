# serializers.py
from rest_framework import serializers
from .models import ClothProduct, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image')

class ClothProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)  # Update the source here

    class Meta:
        model = ClothProduct
        fields = '__all__'
