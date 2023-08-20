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
from ..modules.read_api import *
from app_admins.models import AdminSetting
from concurrent.futures import ThreadPoolExecutor

def datetime_f(data):
    gmt_offset = 7
    data["date_unix"] =  datetime.datetime.utcfromtimestamp(data["date_unix"]) + \
                                datetime.timedelta(hours=gmt_offset)

        # Format the datetime as a string
    data["date_unix"] = data["date_unix"].strftime('%Y-%m-%d %H:%M:%S')
    data["time_unix"] = data["date_unix"].split(" ")[1]
    data["time_unix"] = ":".join(data["time_unix"].split(":")[:2])
    data["date_unix"] = data["date_unix"].split(" ")[0]
    return data


def match_filter(matchs,league_id):
    key_sub = ['id', 'homeID', 'awayID', 'season', 'status', 'roundID', 'game_week', 'homeGoals',
     'awayGoals', 'homeGoalCount', 'awayGoalCount', 'team_a_yellow_cards',
     'team_b_yellow_cards', 'team_a_red_cards', 'team_b_red_cards', 'stadium_name', 'date_unix',
     'winningTeam', 'team_a_dangerous_attacks', 'team_b_dangerous_attacks', 'team_a_attacks',
     'team_b_attacks', 'team_a_xg', 'team_b_xg', 'team_a_penalties_won', 'team_b_penalties_won',
     'team_a_penalty_goals', 'team_b_penalty_goals', 'team_a_penalty_missed', 'team_b_penalty_missed',
     'team_a_throwins', 'team_b_throwins', 'team_a_freekicks', 'team_b_freekicks', 'team_a_goalkicks',
     'team_b_goalkicks', 'home_name', 'away_name','home_image','away_image']
    matchs = {k: matchs[k] for k in key_sub}
    matchs["league_id"] = league_id
    matchs["home_image"] = matchs["home_image"].split("/")[-1]

    matchs["away_image"] = matchs["away_image"].split("/")[-1]
    return matchs
    
def league_match(setting, league_id = 7704):
    
    league_list, api, key = setting.league_list, setting.web_api, setting.api_key
    league_list = [x.strip().replace("-","").replace("  "," ") for x in league_list.split("\n")]
    r = requests.get(f"{api}league-matches?key={key}&season_id={league_id}")
    data = r.json()
    
    if data['success']:
        data = data["data"]
    else:
        data = []
    data = list(map(lambda data: convert_datetime(datetime_f(match_filter(data, league_id))),data))
    # data = list(map(,data))
    # data = list(map(,data))
    return data



def convert_datetime(data):
    
    data["date_unix_thai"] = thai_strftime(datetime.datetime.strptime(data["date_unix"], '%Y-%m-%d').date(), "%e %B %Y")
    return data


def add_match(match, timestamp_now):
    
    defaults = {
    "round_id":match['roundID'], 
    "game_week":match['game_week'], 
    "home_goals":match['homeGoals'],
    "away_goals":match['awayGoals'],  
    "team_a_yellow_cards":match['team_a_yellow_cards'],
    "team_b_yellow_cards":match['team_b_yellow_cards'], 
    "team_a_red_cards":match['team_a_red_cards'], 
    "team_b_red_cards":match['team_b_red_cards'], 
    "stadium_name":match['stadium_name'], 
    "team_a_dangerous_attacks":match['team_a_dangerous_attacks'], 
    "team_b_dangerous_attacks":match['team_b_dangerous_attacks'], 
    "team_a_attacks":match['team_a_attacks'],
    "team_b_attacks":match['team_b_attacks'], 
    "team_a_xg":match['team_a_xg'], 
    "team_b_xg":match['team_b_xg'], 
    "team_a_penalties_won":match['team_a_penalties_won'], 
    "team_b_penalties_won":match['team_b_penalties_won'],
    "team_a_penalty_goals":match['team_a_penalty_goals'], 
    "team_b_penalty_goals":match['team_b_penalty_goals'], 
    "team_a_penalty_missed":match['team_a_penalty_missed'], 
    "team_b_penalty_missed":match['team_b_penalty_missed'],
    "team_a_throwins":match['team_a_throwins'], 
    "team_b_throwins":match['team_b_throwins'], 
    "team_a_freekicks":match['team_a_freekicks'],
    "team_b_freekicks":match['team_b_freekicks'], 
    "team_a_goalkicks":match['team_a_goalkicks'],
    "team_b_goalkicks":match['team_b_goalkicks'],
    "date_unix" : match["date_unix"],
    "date_unix_thai" : match["date_unix_thai"],
    "home_id" : match["homeID"],
    "away_id" : match["awayID"],
    "season" : match["season"],
    "status" : match["status"],
    "home_goal_count" : match["homeGoalCount"],
    "away_goal_count" : match["awayGoalCount"],
    "winning_team" : match["winningTeam"],
    "home_name" : match["home_name"],
    "away_name" : match["away_name"],
    "home_image" : match["home_image"].split("/")[-1],
    "away_image" : match["away_image"].split("/")[-1],
    "time_unix" : match["time_unix"],
    "date_update" : timestamp_now,
    }

    FootballMatch.objects.update_or_create(
        league_id=match["league_id"],
        match_id=match["id"],
        defaults=defaults
    )
def save_all_matchs(league_id):
    setting = AdminSetting.objects.first()
    # FootballMatch.objects.all().delete()
    
    # print(data)
    timestamp_now = int(time.time())
    try:
        latest_entry = FootballMatch.objects.filter(league_id = league_id).latest('date_update').date_update
    except:
        latest_entry = 0
    if abs(latest_entry - timestamp_now) > int(setting.time_matches_update*60):
        data = league_match(setting,league_id = league_id)
        with ThreadPoolExecutor() as executor:
            executor.map(lambda x: add_match(x,timestamp_now), data)
        # for x in data:
        #     add_match(x,timestamp_now)



def get_all_matchs(league_id, date_unix_gte = "2022-08-06",
                    date_unix_lte = "2022-09-03"):
    
    if league_id == "0" or league_id == 0 :
        league = {"name": "", "country":""}
    else:
        league = (FootballLeague.objects.filter(league_id_last=league_id) | \
        FootballLeague.objects.filter(league_id_prev=league_id)).first()
    gmt_offset = 7

    if date_unix_gte == "" and date_unix_lte == "":
        today = datetime.datetime.now()
        date_unix_gte = (today - timedelta(days=7)).strftime("%Y-%m-%d")
        date_unix_lte = today.strftime("%Y-%m-%d")
    elif date_unix_gte == "":
        date_unix_gte = (datetime.datetime.strptime(date_unix_lte, "%Y-%m-%d") - timedelta(days=7)).strftime("%Y-%m-%d")
    elif date_unix_lte == "":
        date_unix_lte = (datetime.datetime.strptime(date_unix_gte, "%Y-%m-%d") + timedelta(days=7)).strftime("%Y-%m-%d")

    if league_id == "0" or league_id == 0 :
        data = FootballMatch.objects.filter(date_unix__gte = date_unix_gte,
            date_unix__lte = date_unix_lte)
    else:
        data = FootballMatch.objects.filter(
    date_unix__gte=date_unix_gte, 
    date_unix__lte=date_unix_lte, 
    league_id=league.league_id_last) | FootballMatch.objects.filter(
        date_unix__gte=date_unix_gte, 
    date_unix__lte=date_unix_lte, 
    league_id=league.league_id_prev
    )
    l= FootballLeague.objects.all().values()
    l = [{'name':x['name'],'league_id_last':x['league_id_last'],
    'league_id_prev':x['league_id_prev']} for x in l]
    result_dict = {league['league_id_last']: league['name'] for league in l}
    result_dict.update({league['league_id_prev']: league['name'] for league in l})

    data1 = list(data.values())
    # print(data)


    data1.sort(key=itemgetter('date_unix'))

    data1 = [list(g) for k, g in groupby(data1, key=itemgetter('date_unix'))][::-1]
    # print(data)



    
    data2 = list(data.values())
    data2 = [{**x, **{"name": result_dict[x['league_id']]}} for x in data2]
    data2.sort(key=itemgetter('date_unix'))
    data2 = [x for x in data2]

    data2 = [list(g) for k, g in groupby(data2, key=itemgetter('name'))]
    return data1, league,data2
