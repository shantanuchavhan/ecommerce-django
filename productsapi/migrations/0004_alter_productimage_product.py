# Generated by Django 5.0.1 on 2024-01-15 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapi', '0003_remove_clothproduct_image_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='productsapi.clothproduct'),
        ),
    ]
