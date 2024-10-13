# Generated by Django 5.1.1 on 2024-10-13 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0002_alter_czynnoscprzetwarzania_czn_status_zatw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='czynnoscprzetwarzania',
            name='czn_zrodlo_danych',
            field=models.CharField(choices=[('OSOBA', 'Bezpośrednio od osoby, której dane dotyczą'), ('INNI', 'Od innej osoby, niż osoba której dane dotyczą'), ('RÓŻNE', 'Od osoby, której dane dotyczą lub od innych osób')], max_length=100, null=True),
        ),
    ]
