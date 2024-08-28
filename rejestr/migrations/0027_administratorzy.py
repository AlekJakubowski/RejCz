# Generated by Django 4.2.4 on 2023-09-29 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0026_czynnoscprzetwarzania_przeslankalegalnosci"),
    ]

    operations = [
        migrations.CreateModel(
            name="Administratorzy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "adm_czynnoscp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rejestr.czynnoscprzetwarzania",
                    ),
                ),
                (
                    "adm_organizacja",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rejestr.organizacja",
                    ),
                ),
            ],
        ),
    ]