# Generated by Django 5.1 on 2024-08-10 14:36

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="retailnetwork",
            name="contacts",
        ),
        migrations.RemoveField(
            model_name="factory",
            name="contacts",
        ),
        migrations.RemoveField(
            model_name="individualentrepreneur",
            name="contacts",
        ),
        migrations.RemoveField(
            model_name="factory",
            name="products",
        ),
        migrations.RemoveField(
            model_name="retailnetwork",
            name="supplier",
        ),
        migrations.RemoveField(
            model_name="individualentrepreneur",
            name="products",
        ),
        migrations.RemoveField(
            model_name="individualentrepreneur",
            name="supplier_content_type",
        ),
        migrations.RemoveField(
            model_name="retailnetwork",
            name="products",
        ),
        migrations.CreateModel(
            name="NetworkNode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Название")),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="Email"
                    ),
                ),
                ("country", models.CharField(max_length=50, verbose_name="Страна")),
                ("city", models.CharField(max_length=50, verbose_name="Город")),
                ("street", models.CharField(max_length=50, verbose_name="Улица")),
                ("house_number", models.CharField(max_length=10, verbose_name="Дом")),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Дебеторская задолженность",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        default=datetime.date(2024, 8, 10), verbose_name="Дата создания"
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="suppliers.networknode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сетевой узел",
                "verbose_name_plural": "Сетевые узлы",
            },
        ),
        migrations.AddField(
            model_name="products",
            name="network_node",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="suppliers.networknode",
                verbose_name="Торгующая сеть",
            ),
        ),
        migrations.DeleteModel(
            name="Contacts",
        ),
        migrations.DeleteModel(
            name="Factory",
        ),
        migrations.DeleteModel(
            name="IndividualEntrepreneur",
        ),
        migrations.DeleteModel(
            name="RetailNetwork",
        ),
    ]
