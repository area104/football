from footballresults.models import FootballMatch, FootballLeague
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
    if league is None:
        print(league, league_id)

    
    data = (FootballMatch.objects.filter(league_id=league_id, match_id = match_id) | \
    FootballMatch.objects.filter(league_id=league.league_id_prev, match_id = match_id)
    )
    
    data = data.first()
    
    return data

            