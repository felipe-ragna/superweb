# Generated by Django 4.1 on 2024-10-21 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='detalles',
        ),
    ]