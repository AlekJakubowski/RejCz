# Generated by Django 5.1.1 on 2024-11-06 15:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0012_profiluzytkownika_pro_komorka'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfilUzytkownika',
            new_name='Profile',
        ),
    ]
