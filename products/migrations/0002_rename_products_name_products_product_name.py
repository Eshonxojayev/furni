# Generated by Django 5.0.6 on 2024-06-17 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='products_name',
            new_name='product_name',
        ),
    ]
