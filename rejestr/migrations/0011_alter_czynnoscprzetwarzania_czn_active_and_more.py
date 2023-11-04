# Generated by Django 4.2.4 on 2023-09-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0010_alter_czynnoscprzetwarzania_czn_status_zatw_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="czynnoscprzetwarzania",
            name="czn_active",
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name="czynnoscprzetwarzania",
            name="czn_status_zatw",
            field=models.CharField(
                choices=[
                    ("-----------", "-----------"),
                    ("OCZEKUJĄCA", "OCZEKUJĄCA"),
                    ("ANULOWANA", "ANULOWANA"),
                    ("ODRZUCONA", "ODRZUCONA"),
                    ("ZATWIERDZONA", "ZATWIERDZONA"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="czynnoscprzetwarzania",
            name="czn_zrodlo_danych",
            field=models.CharField(
                choices=[
                    (
                        "Bezpośrednio od osoby, której dane dotyczą",
                        "Bezpośrednio od osoby, której dane dotyczą",
                    ),
                    (
                        "Od innej osoby, niż osoba której dane dotyczą",
                        "Od innej osoby, niż osoba której dane dotyczą",
                    ),
                    (
                        "Od osoby, której dane dotyczą lub od innych osób",
                        "Od osoby, której dane dotyczą lub od innych osób",
                    ),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]
