# Generated by Django 5.1.1 on 2024-11-01 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0007_alter_grupazabezpieczen_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='komorkiprofilu',
            name='kpu_profil_u',
        ),
        migrations.AddField(
            model_name='komorkiprofilu',
            name='kpu_profil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rejestr.profiluzytkownika'),
        ),
        migrations.AlterField(
            model_name='komorkiprofilu',
            name='kpu_komorka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rejestr.komorka'),
        ),
        migrations.CreateModel(
            name='RejestryKomorki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rko_komorka', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rejestr.komorka')),
                ('rko_rejestr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rejestr.rejestr')),
            ],
            options={
                'verbose_name': 'Rejestr komórki',
                'verbose_name_plural': 'Rejestry komórek',
            },
        ),
        migrations.AddField(
            model_name='komorka',
            name='RejestryKomorki',
            field=models.ManyToManyField(related_name='Komorki_Rejestry', through='rejestr.RejestryKomorki', to='rejestr.rejestr'),
        ),
    ]
