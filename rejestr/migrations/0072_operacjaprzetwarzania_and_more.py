# Generated by Django 4.2.4 on 2024-01-07 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0071_operacjeprzetwarzania'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperacjaPrzetwarzania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opp_active', models.BooleanField(default=True, null=True)),
                ('opp_opis', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='OperacjePrzetwarzania',
            field=models.ManyToManyField(related_name='CzynnoscPrzetwarzania_OperacjePrzetwarzania', through='rejestr.OperacjePrzetwarzania', to='rejestr.operacjaprzetwarzania'),
        ),
        migrations.AlterField(
            model_name='operacjeprzetwarzania',
            name='opp_operacjap',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opp_operacjap_p', to='rejestr.operacjaprzetwarzania'),
        ),
    ]
