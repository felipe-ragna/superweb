# Generated by Django 5.1.3 on 2024-11-16 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0006_mercancia_tipomercancias_alter_juego_tipomercancias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mercancia',
            name='detail',
            field=models.TextField(default='', verbose_name='Detalle producto'),
            preserve_default=False,
        ),
    ]
