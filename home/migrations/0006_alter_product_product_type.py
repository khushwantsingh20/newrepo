# Generated by Django 4.2.6 on 2023-11-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, choices=[('phone', 'Phone'), ('laptop', 'Laptop'), ('keyboard', 'Keyboard'), ('book', 'Book'), ('tshirt', 'T-Shirt'), ('pants', 'Pants'), ('mouse', 'Mouse'), ('shoes', 'Shoes'), ('bags', 'Bags')], max_length=10, null=True),
        ),
    ]
