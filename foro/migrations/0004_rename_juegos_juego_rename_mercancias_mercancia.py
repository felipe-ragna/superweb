# Generated by Django 5.1.3 on 2024-11-16 20:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0003_tipomercancia_juegos_mercancias'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='juegos',
            new_name='juego',
        ),
        migrations.RenameModel(
            old_name='mercancias',
            new_name='mercancia',
        ),
    ]
