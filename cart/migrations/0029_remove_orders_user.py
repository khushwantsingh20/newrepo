# Generated by Django 4.2.6 on 2023-12-18 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0028_orders_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='user',
        ),
    ]
