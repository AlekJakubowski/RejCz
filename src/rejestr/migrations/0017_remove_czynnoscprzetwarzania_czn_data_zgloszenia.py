# Generated by Django 5.1.1 on 2024-12-07 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0016_remove_czynnoscprzetwarzania_czn_status_zatw_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='czynnoscprzetwarzania',
            name='czn_data_zgloszenia',
        ),
    ]
