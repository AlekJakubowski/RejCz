# Generated by Django 4.2.4 on 2023-10-25 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0064_podatnosc_ryzyko_zakresoddzialywania_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ryzyko',
            name='Zabezpieczenie',
            field=models.ManyToManyField(to='rejestr.zabezpieczenie'),
        ),
        migrations.AddField(
            model_name='ryzyko',
            name='Zagrozenie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rejestr.zagrozenie'),
        ),
        migrations.AddField(
            model_name='ryzyko',
            name='ZakresOddzialywania',
            field=models.ManyToManyField(to='rejestr.zakresoddzialywania'),
        ),
    ]