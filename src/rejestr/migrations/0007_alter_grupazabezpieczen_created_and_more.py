# Generated by Django 5.1.1 on 2024-10-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0006_alter_administratorzy_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupazabezpieczen',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='grupazabezpieczen',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
