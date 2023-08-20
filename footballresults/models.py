from djongo import models


class FootballMatch(models.Model):
    _id = models.ObjectIdField()
    league_id = models.IntegerField()
    match_id = models.IntegerField()
    round_id  = models.IntegerField()
    game_week  = models.IntegerField()
    home_goals=models.JSONField()
    away_goals=models.JSONField()
    team_a_yellow_cards=models.IntegerField()
    team_b_yellow_cards=models.IntegerField()
    team_a_red_cards=models.IntegerField()
    team_b_red_cards=models.IntegerField()
    stadium_name =models.CharField(max_length=100)
    team_a_dangerous_attacks =models.IntegerField()
    team_b_dangerous_attacks =models.IntegerField()
    team_a_attacks=models.IntegerField()
    team_b_attacks =models.IntegerField()
    team_a_xg=models.FloatField()
    team_b_xg=models.FloatField()
    team_a_penalties_won= models.IntegerField()
    team_b_penalties_won=models.IntegerField()
    team_a_penalty_goals= models.IntegerField()
    team_b_penalty_goals= models.IntegerField()
    team_a_penalty_missed= models.IntegerField()
    team_b_penalty_missed=models.IntegerField()
    team_a_throwins= models.IntegerField()
    team_b_throwins= models.IntegerField()
    team_a_freekicks= models.IntegerField()
    team_b_freekicks= models.IntegerField()
    team_a_goalkicks=models.IntegerField()
    team_b_goalkicks=models.IntegerField()
    date_unix = models.CharField(max_length=100)
    date_unix_thai = models.CharField(max_length=100)
    time_unix = models.CharField(max_length=100)
    home_id = models.IntegerField()
    away_id = models.IntegerField()
    season = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    home_goal_count = models.IntegerField()
    away_goal_count = models.IntegerField()
    winning_team = models.CharField(max_length=100)
    home_name = models.CharField(max_length=100)
    away_name = models.CharField(max_length=100)
    home_image = models.CharField(max_length=100)
    away_image = models.CharField(max_length=100)
    date_update = models.IntegerField()

    class Meta:
        db_table = 'football_match'

    def __str__(self):
        return f"{self.match_id} vs {self.away_image}"


class FootballLeague(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    league_id_last = models.IntegerField()
    league_id_prev = models.IntegerField()
    date_update = models.IntegerField()

    class Meta:
        db_table = 'football_league'

    def __str__(self):
        return f"self.name vs self.league_id"

class FootballTeams(models.Model):
    _id = models.ObjectIdField()
    id= models.IntegerField()
    name = models.CharField(max_length=200)
    cleanName = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)
    shortHand = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    founded = models.IntegerField()
    image = models.CharField(max_length=200)
    season = models.CharField(max_length=200)
    table_position = models.IntegerField()
    performance_rank = models.IntegerField()
    risk = models.IntegerField()
    season_format  = models.CharField(max_length=200)
    competition_id = models.IntegerField()
    full_name = models.CharField(max_length=200)
    season_id = models.IntegerField()
    stats_seasonMatchesPlayed_away = models.IntegerField()
    stats_seasonWinsNum_away = models.IntegerField()
    stats_seasonFTS_away = models.IntegerField()
    stats_seasonDrawsNum_home = models.IntegerField()
    stats_losePercentage_overall = models.IntegerField()
    stats_losePercentage_away = models.IntegerField()
    stats_leaguePosition_away = models.IntegerField()
    stats_prediction_risk = models.IntegerField()
    stats_leaguePosition_home = models.IntegerField()
    stats_seasonConcededNum_overall = models.IntegerField()
    stats_seasonFTS_home = models.IntegerField()
    stats_seasonFTS_overall = models.IntegerField()
    stats_seasonLossesNum_overall = models.IntegerField()
    stats_seasonScoredNum_away = models.IntegerField()
    stats_seasonMatchesPlayed_overall = models.IntegerField()
    stats_seasonWinsNum_home = models.IntegerField()
    stats_seasonGoalDifference_overall = models.IntegerField()
    stats_name_th = models.CharField(max_length=200)
    stats_leaguePosition_overall = models.IntegerField()
    stats_suspended_matches= models.IntegerField()
    stats_drawPercentage_overall= models.IntegerField()
    stats_seasonGoalDifference_away = models.IntegerField()
    stats_seasonConcededNum_away= models.IntegerField()
    stats_seasonGoalsTotal_away = models.IntegerField()
    stats_seasonGoalsTotal_home = models.IntegerField()
    stats_seasonWinsNum_overall = models.IntegerField()
    stats_seasonLossesNum_home = models.IntegerField()
    stats_seasonDrawsNum_away= models.IntegerField()
    stats_losePercentage_home = models.IntegerField()
    stats_seasonGoalsTotal_overall = models.IntegerField()
    stats_winPercentage_home = models.IntegerField()
    stats_drawPercentage_away = models.IntegerField()
    stats_winPercentage_overall = models.IntegerField()
    stats_drawPercentage_home= models.IntegerField()
    stats_seasonScoredNum_overall = models.IntegerField()
    stats_seasonLossesNum_away = models.IntegerField()
    stats_seasonDrawsNum_overall = models.IntegerField()
    stats_seasonGoalDifference_home = models.IntegerField()
    stats_seasonMatchesPlayed_home = models.IntegerField()
    stats_winPercentage_away = models.IntegerField()
    stats_seasonScoredNum_home = models.IntegerField()
    stats_seasonConcededNum_home= models.IntegerField()

    class Meta:
        db_table = 'football_teams'

    def __str__(self):
        return f"self.name vs self.league_id"

class FootballTeamStat(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    # league_id = models.CharField(max_length=200)
    # league_year = models.CharField(max_length=200)
    # image = models.CharField(max_length=200)
    # country = models.CharField(max_length=200)

    class Meta:
        db_table = 'football_teams_stat'

    def __str__(self):
        return f"self.name vs self.league_id"

