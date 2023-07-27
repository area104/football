# Generated by Django 4.1.10 on 2023-07-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("footballresults", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FootballMatch",
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
                ("home_team", models.CharField(max_length=100)),
                ("home_score", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "football_match",
            },
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]