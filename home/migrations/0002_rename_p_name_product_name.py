# Generated by Django 4.2.6 on 2023-11-06 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='p_name',
            new_name='name',
        ),
    ]
