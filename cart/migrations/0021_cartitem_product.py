# Generated by Django 4.2.6 on 2023-12-18 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_product_product_type'),
        ('cart', '0020_remove_cartitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
    ]
