# Generated by Django 4.2.6 on 2023-12-25 06:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
