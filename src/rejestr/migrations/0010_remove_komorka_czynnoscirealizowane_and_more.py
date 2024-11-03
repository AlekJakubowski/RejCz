# Generated by Django 5.1.1 on 2024-11-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0009_organizacja_org_kod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='komorka',
            name='CzynnosciRealizowane',
        ),
        migrations.AlterField(
            model_name='rejestr',
            name='rej_zakres',
            field=models.CharField(choices=[('RODO', 'Rozporządzenie 679/2016, przetwarzanie ogólne'), ('DODO', 'Dyrektywa 680/2016, przetwarzanie policyjne')], default='RODO', max_length=50, null=True),
        ),
    ]
