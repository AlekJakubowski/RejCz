# Generated by Django 4.2.4 on 2023-10-14 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0053_czynnoscprzetwarzania_komorkirealizujace_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='czynnoscprzetwarzania',
            name='KomorkiRealizujace',
            field=models.ManyToManyField(null=True, related_name='CzynnoscPrzetwarzania_Komorki', through='rejestr.CzynnosciPrzetwarzania', to='rejestr.komorka'),
        ),
    ]
