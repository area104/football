# Generated by Django 4.1.10 on 2023-08-18 12:55

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FootballLeague",
            fields=[
                (
                    "_id",
                    djongo.models.fields.ObjectIdField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("image", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=200)),
                ("league_id_last", models.IntegerField()),
                ("league_id_prev", models.IntegerField()),
                ("date_update", models.IntegerField()),
            ],
            options={
                "db_table": "football_league",
            },
        ),
        migrations.CreateModel(
            name="FootballMatch",
            fields=[
                (
                    "_id",
                    djongo.models.fields.ObjectIdField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("league_id", models.IntegerField()),
                ("match_id", models.IntegerField()),
                ("round_id", models.IntegerField()),
                ("game_week", models.IntegerField()),
                ("home_goals", djongo.models.fields.JSONField()),
                ("away_goals", djongo.models.fields.JSONField()),
                ("team_a_yellow_cards", models.IntegerField()),
                ("team_b_yellow_cards", models.IntegerField()),
                ("team_a_red_cards", models.IntegerField()),
                ("team_b_red_cards", models.IntegerField()),
                ("stadium_name", models.CharField(max_length=100)),
                ("team_a_dangerous_attacks", models.IntegerField()),
                ("team_b_dangerous_attacks", models.IntegerField()),
                ("team_a_attacks", models.IntegerField()),
                ("team_b_attacks", models.IntegerField()),
                ("team_a_xg", models.FloatField()),
                ("team_b_xg", models.FloatField()),
                ("team_a_penalties_won", models.IntegerField()),
                ("team_b_penalties_won", models.IntegerField()),
                ("team_a_penalty_goals", models.IntegerField()),
                ("team_b_penalty_goals", models.IntegerField()),
                ("team_a_penalty_missed", models.IntegerField()),
                ("team_b_penalty_missed", models.IntegerField()),
                ("team_a_throwins", models.IntegerField()),
                ("team_b_throwins", models.IntegerField()),
                ("team_a_freekicks", models.IntegerField()),
                ("team_b_freekicks", models.IntegerField()),
                ("team_a_goalkicks", models.IntegerField()),
                ("team_b_goalkicks", models.IntegerField()),
                ("date_unix", models.CharField(max_length=100)),
                ("date_unix_thai", models.CharField(max_length=100)),
                ("time_unix", models.CharField(max_length=100)),
                ("home_id", models.IntegerField()),
                ("away_id", models.IntegerField()),
                ("season", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                ("home_goal_count", models.IntegerField()),
                ("away_goal_count", models.IntegerField()),
                ("winning_team", models.CharField(max_length=100)),
                ("home_name", models.CharField(max_length=100)),
                ("away_name", models.CharField(max_length=100)),
                ("home_image", models.CharField(max_length=100)),
                ("away_image", models.CharField(max_length=100)),
                ("date_update", models.IntegerField()),
            ],
            options={
                "db_table": "football_match",
            },
        ),
        migrations.CreateModel(
            name="FootballTeams",
            fields=[
                (
                    "_id",
                    djongo.models.fields.ObjectIdField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("id", models.IntegerField()),
                ("name", models.CharField(max_length=200)),
                ("cleanName", models.CharField(max_length=200)),
                ("english_name", models.CharField(max_length=200)),
                ("shortHand", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=200)),
                ("founded", models.IntegerField()),
                ("image", models.CharField(max_length=200)),
                ("season", models.CharField(max_length=200)),
                ("table_position", models.IntegerField()),
                ("performance_rank", models.IntegerField()),
                ("risk", models.IntegerField()),
                ("season_format", models.CharField(max_length=200)),
                ("competition_id", models.IntegerField()),
                ("full_name", models.CharField(max_length=200)),
                ("season_id", models.IntegerField()),
                ("stats_seasonMatchesPlayed_away", models.IntegerField()),
                ("stats_seasonWinsNum_away", models.IntegerField()),
                ("stats_seasonFTS_away", models.IntegerField()),
                ("stats_seasonDrawsNum_home", models.IntegerField()),
                ("stats_losePercentage_overall", models.IntegerField()),
                ("stats_losePercentage_away", models.IntegerField()),
                ("stats_leaguePosition_away", models.IntegerField()),
                ("stats_prediction_risk", models.IntegerField()),
                ("stats_leaguePosition_home", models.IntegerField()),
                ("stats_seasonConcededNum_overall", models.IntegerField()),
                ("stats_seasonFTS_home", models.IntegerField()),
                ("stats_seasonFTS_overall", models.IntegerField()),
                ("stats_seasonLossesNum_overall", models.IntegerField()),
                ("stats_seasonScoredNum_away", models.IntegerField()),
                ("stats_seasonMatchesPlayed_overall", models.IntegerField()),
                ("stats_seasonWinsNum_home", models.IntegerField()),
                ("stats_seasonGoalDifference_overall", models.IntegerField()),
                ("stats_name_th", models.CharField(max_length=200)),
                ("stats_leaguePosition_overall", models.IntegerField()),
                ("stats_suspended_matches", models.IntegerField()),
                ("stats_drawPercentage_overall", models.IntegerField()),
                ("stats_seasonGoalDifference_away", models.IntegerField()),
                ("stats_seasonConcededNum_away", models.IntegerField()),
                ("stats_seasonGoalsTotal_away", models.IntegerField()),
                ("stats_seasonGoalsTotal_home", models.IntegerField()),
                ("stats_seasonWinsNum_overall", models.IntegerField()),
                ("stats_seasonLossesNum_home", models.IntegerField()),
                ("stats_seasonDrawsNum_away", models.IntegerField()),
                ("stats_losePercentage_home", models.IntegerField()),
                ("stats_seasonGoalsTotal_overall", models.IntegerField()),
                ("stats_winPercentage_home", models.IntegerField()),
                ("stats_drawPercentage_away", models.IntegerField()),
                ("stats_winPercentage_overall", models.IntegerField()),
                ("stats_drawPercentage_home", models.IntegerField()),
                ("stats_seasonScoredNum_overall", models.IntegerField()),
                ("stats_seasonLossesNum_away", models.IntegerField()),
                ("stats_seasonDrawsNum_overall", models.IntegerField()),
                ("stats_seasonGoalDifference_home", models.IntegerField()),
                ("stats_seasonMatchesPlayed_home", models.IntegerField()),
                ("stats_winPercentage_away", models.IntegerField()),
                ("stats_seasonScoredNum_home", models.IntegerField()),
                ("stats_seasonConcededNum_home", models.IntegerField()),
            ],
            options={
                "db_table": "football_teams",
            },
        ),
        migrations.CreateModel(
            name="FootballTeamStat",
            fields=[
                (
                    "_id",
                    djongo.models.fields.ObjectIdField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "football_teams_stat",
            },
        ),
    ]
