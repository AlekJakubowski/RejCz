# Generated by Django 5.1.1 on 2024-12-07 22:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0023_danawrazliwa_danewrazliwe'),
    ]

    operations = [
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='czn_rodzaje_wrazliwe',
            field=models.ManyToManyField(related_name='DaneaWrazliwa', through='rejestr.DaneWrazliwe', to='rejestr.danawrazliwa'),
        ),
        migrations.AlterField(
            model_name='danewrazliwe',
            name='rdw_dane_w',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rdw_danew_p', to='rejestr.danawrazliwa'),
        ),
    ]