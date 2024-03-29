# Generated by Django 4.2.6 on 2023-11-30 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pimg')),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=10)),
                ('landmark', models.CharField(max_length=250)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
