# Generated by Django 5.1 on 2024-08-10 14:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0002_remove_retailnetwork_contacts_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="networknode",
            name="creation_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата создания"
            ),
        ),
    ]
