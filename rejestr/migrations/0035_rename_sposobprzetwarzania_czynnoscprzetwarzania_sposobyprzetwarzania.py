# Generated by Django 4.2.4 on 2023-09-30 20:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rejestr", "0034_alter_sposobprzetwarzania_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="czynnoscprzetwarzania",
            old_name="SposobPrzetwarzania",
            new_name="SposobyPrzetwarzania",
        ),
    ]
