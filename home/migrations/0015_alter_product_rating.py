# Generated by Django 4.2.6 on 2023-12-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_product_rating_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=5, null=True),
        ),
    ]