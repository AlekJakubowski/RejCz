# Generated by Django 4.2.4 on 2023-09-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0014_remove_czynnoscprzetwarzania_organizacja_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="okresretencji",
            name="okr_lat_max",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
