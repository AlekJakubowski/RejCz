# Generated by Django 4.2.4 on 2023-10-08 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0048_alter_czynnoscprzetwarzania_administratorzy_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kategoriedanych",
            name="ktd_czynnoscp",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ktd_czynnosc_p",
                to="rejestr.czynnoscprzetwarzania",
            ),
        ),
        migrations.AlterField(
            model_name="kategoriedanych",
            name="ktd_dane",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ktd_dane_p",
                to="rejestr.kategoriadanych",
            ),
        ),
        migrations.AlterField(
            model_name="kategorieodbiorcow",
            name="kob_czynnoscp",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="kob_czynnosc_p",
                to="rejestr.czynnoscprzetwarzania",
            ),
        ),
        migrations.AlterField(
            model_name="kategorieodbiorcow",
            name="kob_odbiorcy",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="kob_odbiorcy_p",
                to="rejestr.kategoriaodbiorcow",
            ),
        ),
        migrations.AlterField(
            model_name="kategorieosob",
            name="kos_czynnoscp",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="kos_czynnosc_p",
                to="rejestr.czynnoscprzetwarzania",
            ),
        ),
        migrations.AlterField(
            model_name="kategorieosob",
            name="kos_kosoby",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="kos_kosoby_p",
                to="rejestr.kategoriaosob",
            ),
        ),
    ]
