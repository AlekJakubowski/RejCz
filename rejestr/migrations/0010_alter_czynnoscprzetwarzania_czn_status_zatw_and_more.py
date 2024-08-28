# Generated by Django 4.2.4 on 2023-09-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0009_alter_czynnoscprzetwarzania_czn_status_zatw"),
    ]

    operations = [
        migrations.AlterField(
            model_name="czynnoscprzetwarzania",
            name="czn_status_zatw",
            field=models.CharField(
                choices=[
                    ("-----------", "-----------"),
                    ("ZATWIERDZONA", "ZATWIERDZONA"),
                    ("ANULOWANA", "ANULOWANA"),
                    ("ODRZUCONA", "ODRZUCONA"),
                    ("OCZEKUJĄCA", "OCZEKUJĄCA"),
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
                    ("-----------", "-----------"),
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