# Generated by Django 4.2.4 on 2023-10-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0061_remove_zabezpieczenie_grupazabezpieczen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zabezpieczenie',
            name='Zagrozenie',
        ),
        migrations.AddField(
            model_name='zabezpieczenie',
            name='Zagrozenia',
            field=models.ManyToManyField(to='rejestr.zagrozenie'),
        ),
    ]
