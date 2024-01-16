# views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClothProduct, ProductImage
from .serializers import ClothProductSerializer, ProductImageSerializer
class ClothProductListView(APIView):
    def get(self, request, id=None, category=None):
        # If 'id' is provided, get a single product by ID with related images
        if id:
            cloth_product = get_object_or_404(ClothProduct.objects.prefetch_related('product_images'), id=id)
            serializer = ClothProductSerializer(cloth_product)
            return Response(serializer.data)

        # If 'category' is provided, get a list of products by category with related images
        elif category:
            cloth_products = ClothProduct.objects.filter(category__name__iexact=category).prefetch_related('product_images')
            serializer = ClothProductSerializer(cloth_products, many=True)
            return Response(serializer.data)

        # If no 'id' or 'category' provided, get a list of all products with related images
        else:
            cloth_products = ClothProduct.objects.all().prefetch_related('product_images')
            serializer = ClothProductSerializer(cloth_products, many=True)
            return Response(serializer.data)
