# Generated by Django 4.2.4 on 2023-10-21 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0058_zabezpieczenie_zagrozenie'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupaZabezpieczen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gzb_active', models.BooleanField(default=True)),
                ('gzb_opis', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrupaZagrozen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gzg_active', models.BooleanField(default=True)),
                ('gzg_opis', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='zabezpieczenie',
            name='GrupaZabezpieczen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rejestr.grupazabezpieczen'),
        ),
        migrations.AddField(
            model_name='zagrozenie',
            name='GrupaZagrozen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rejestr.grupazagrozen'),
        ),
    ]
