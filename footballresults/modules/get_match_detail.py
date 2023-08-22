from footballresults.models import FootballMatch, FootballLeague, FootballTeams
import os
from django.conf import settings
import json
import datetime
from pythainlp.util import thai_strftime
from operator import itemgetter
from itertools import groupby
from datetime import timedelta
import requests
import time


def get_match_detail(league_id, match_id):
    league = (FootballLeague.objects.filter(league_id_last=league_id) | \
    FootballLeague.objects.filter(league_id_prev=league_id)).first()


    
    data = (FootballMatch.objects.filter(league_id=league_id, match_id = match_id) | \
    FootballMatch.objects.filter(league_id=league.league_id_prev, match_id = match_id)
    )
    
    data = data.first()
    
    return data


from django.forms.models import model_to_dict


def get_matchdetail(league_id,match_id):
    data = get_match_detail(league_id, match_id)

    teams_home = FootballTeams.objects.filter(season_id=league_id, id = data.home_id).first()
    teams_away = FootballTeams.objects.filter(season_id=league_id, id = data.away_id).first()
    get_team = (teams_home != None and teams_away != None)
    if get_team:
        teams_home = model_to_dict(teams_home)
        teams_away = model_to_dict(teams_away)

        teams = {}
        
        for key in set(teams_home.keys()) - {"_id", "image", "image_url", 
        "competition_id", "competition_id", "date_update"}:
            teams[key] = [teams_home[key], teams_away[key]]


        return {"data":data, "get_team":get_team, "teams": teams}
    else:
        return {"data":data, "get_team":get_team, "teams": {}}

            