# Generated by Django 4.2.6 on 2023-12-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_remove_orders_product_alter_orders_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
