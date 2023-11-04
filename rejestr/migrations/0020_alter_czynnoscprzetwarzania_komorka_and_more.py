# Generated by Django 4.2.4 on 2023-09-29 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0019_delete_zabezpieczenie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="czynnoscprzetwarzania",
            name="Komorka",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="rejestr.komorka",
            ),
        ),
        migrations.AlterField(
            model_name="czynnoscprzetwarzania",
            name="OkresRetencji",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="rejestr.okresretencji",
            ),
        ),
        migrations.AlterField(
            model_name="czynnoscprzetwarzania",
            name="Rejestr",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="rejestr.rejestr",
            ),
        ),
        migrations.AlterField(
            model_name="komorka",
            name="Organizacja",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="rejestr.organizacja",
            ),
        ),
    ]
