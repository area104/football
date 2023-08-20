from django.db import models
from django.contrib.auth.models import User

class AdminSetting(models.Model):
    web_api = models.CharField(max_length=1023)
    api_key = models.CharField(max_length=1023)
    date_update = models.IntegerField()
    line_api = models.CharField(max_length=1023)
    userid = models.IntegerField()
    time_league_update = models.IntegerField()
    time_time_update = models.IntegerField()
    time_matches_update = models.IntegerField()
    league_list = models.TextField()




    class Meta:
        db_table = 'db_admin_setting'

    def __str__(self):
        return self.username