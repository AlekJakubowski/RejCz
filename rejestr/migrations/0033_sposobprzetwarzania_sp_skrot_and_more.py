# Generated by Django 4.2.4 on 2023-09-30 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0032_czynnoscprzetwarzania_podmiotyprzetwarzajace_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sposobprzetwarzania",
            name="sp_skrot",
            field=models.CharField(null=False, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sposobprzetwarzania",
            name="sp_opis",
            field=models.CharField(null=True, max_length=300),
        ),
    ]
