# urls.py
from django.urls import path
from .views import ClothProductListView

urlpatterns = [
    path('api/cloth_products/', ClothProductListView.as_view(), name='cloth-product-list'),
    path('api/cloth_products/<str:id>/', ClothProductListView.as_view(), name='cloth-product-list'),
    path('api/categories/<str:category>/', ClothProductListView.as_view(), name='category-cloth-product-list'),
]
