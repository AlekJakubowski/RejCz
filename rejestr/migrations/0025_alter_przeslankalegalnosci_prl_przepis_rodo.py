# Generated by Django 4.2.4 on 2023-09-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0024_alter_przeslankalegalnosci_prl_przepis_rodo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="przeslankalegalnosci",
            name="prl_przepis_rodo",
            field=models.CharField(max_length=500, null=True),
        ),
    ]