# Generated by Django 4.2.4 on 2023-10-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0040_alter_kategoriadanych_kd_opis"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wysokieryzyka",
            name="wr_opis",
            field=models.TextField(max_length=300),
        ),
    ]
