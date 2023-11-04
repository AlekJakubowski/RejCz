# Generated by Django 4.2.4 on 2023-09-27 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0007_remove_kategoriadanych_slug_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_administratorzy",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_kategorie_danych",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_komorki",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_okres_retencji",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_podmioty_przetw",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_przeslanki_legalnosci",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_przeslanki_wys_ryz",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_rej_id",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_sposoby_przetw",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_wspoladm",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_zabezp_admin",
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="czn_zabezp_transf",
        ),
        migrations.AddField(
            model_name="czynnoscprzetwarzania",
            name="OkresRetencji",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="rejestr.okresretencji",
            ),
        ),
        migrations.AddField(
            model_name="czynnoscprzetwarzania",
            name="Organizacja",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="rejestr.organizacja",
            ),
        ),
        migrations.RemoveField(
            model_name="czynnoscprzetwarzania",
            name="Komorka",
        ),
        migrations.AlterField(
            model_name="czynnoscprzetwarzania",
            name="czn_opis_celu",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="czynnoscprzetwarzania",
            name="czn_podstawa_prawna",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="czynnoscprzetwarzania",
            name="czn_przepis_wrazliwe",
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name="czynnoscprzetwarzania",
            name="Komorka",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="rejestr.komorka",
            ),
        ),
    ]
