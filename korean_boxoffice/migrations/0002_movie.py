# Generated by Django 5.2 on 2025-04-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("korean_boxoffice", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("movie_name", models.CharField(max_length=255)),
            ],
        ),
    ]
