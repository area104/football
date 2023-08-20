# Generated by Django 4.1.10 on 2023-08-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminSetting",
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
                ("web_api", models.CharField(max_length=1023)),
                ("api_key", models.CharField(max_length=1023)),
                ("date_update", models.IntegerField()),
                ("line_api", models.CharField(max_length=1023)),
                ("userid", models.IntegerField()),
                ("time_league_update", models.IntegerField()),
                ("time_time_update", models.IntegerField()),
                ("time_matches_update", models.IntegerField()),
                ("league_list", models.TextField()),
            ],
            options={
                "db_table": "db_admin_setting",
            },
        ),
    ]