from djongo import models

class FootballMatch(models.Model):
    _id = models.ObjectIdField()
    match_id = models.CharField(max_length=100)
    date_unix = models.CharField(max_length=100)
    time_unix = models.CharField(max_length=100)
    home_id = models.CharField(max_length=100)
    away_id = models.CharField(max_length=100)
    league_id = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    home_goal_count = models.IntegerField()
    away_goal_count = models.IntegerField()
    winning_team = models.CharField(max_length=100)
    home_name = models.CharField(max_length=100)
    away_name = models.CharField(max_length=100)
    home_image = models.CharField(max_length=100)
    away_image = models.CharField(max_length=100)

    class Meta:
        db_table = 'football_match'

    def __str__(self):
        return f"{self.match_id} vs {self.away_image}"

class FootballLeague(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    league_id = models.CharField(max_length=200)
    league_year = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    class Meta:
        db_table = 'football_league'

    def __str__(self):
        return f"{self.name} vs {self.league_id}"
