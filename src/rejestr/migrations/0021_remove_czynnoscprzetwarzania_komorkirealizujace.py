# Generated by Django 5.1.1 on 2024-12-07 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0020_remove_czynnoscprzetwarzania_rejestr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='czynnoscprzetwarzania',
            name='KomorkiRealizujace',
        ),
    ]
