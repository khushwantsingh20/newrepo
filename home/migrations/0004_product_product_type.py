# Generated by Django 4.2.6 on 2023-11-08 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, choices=[('phone', 'Phone'), ('laptop', 'Laptop'), ('keyboard', 'Keyboard'), ('book', 'Book'), ('tshirt', 'T-Shirt'), ('pants', 'Pants'), ('mouse', 'Mouse')], max_length=10, null=True),
        ),
    ]