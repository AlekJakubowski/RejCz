# Generated by Django 4.2.4 on 2023-10-01 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0044_remove_wysokieryzyka_created_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="czynnoscprzetwarzania",
            name="WysokieRyzyka",
            field=models.ManyToManyField(
                related_name="CzynnoscPrzetwarzania_WysokieRyzyko",
                through="rejestr.WysokieRyzyka",
                to="rejestr.wysokieryzyko",
            ),
        ),
        migrations.CreateModel(
            name="PrzeslankiLegalnosci",
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
                    "ppl_czynnoscp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ppl_czynnosc_p",
                        to="rejestr.czynnoscprzetwarzania",
                    ),
                ),
                (
                    "ppl_przeslankap",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ppl_przeslanka_p",
                        to="rejestr.przeslankalegalnosci",
                    ),
                ),
            ],
        ),
    ]
