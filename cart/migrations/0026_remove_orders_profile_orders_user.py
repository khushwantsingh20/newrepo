# Generated by Django 4.2.6 on 2023-12-18 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0025_remove_cartitem_profile_cartitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='profile',
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]