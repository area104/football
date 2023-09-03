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
from app_admins.models import AdminSetting
from concurrent.futures import ThreadPoolExecutor
from .linenotify import *

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
     'team_b_goalkicks', 'home_name', 'away_name','home_image','away_image',
     "home_ppg","away_ppg","pre_match_home_ppg","pre_match_away_ppg",
    "pre_match_teamA_overall_ppg","pre_match_teamB_overall_ppg"]
    matchs = {k: matchs[k] for k in key_sub}
    matchs["league_id"] = league_id
    matchs["home_image"] = matchs["home_image"]

    matchs["away_image"] = matchs["away_image"]
    return matchs
    
def league_match(setting, league_id = 7704):
    try:
        league_list, api, key = setting.league_list, setting.web_api, setting.api_key
        league_list = [x.strip().replace("-","").replace("  "," ") for x in league_list.split("\n")]
        r = requests.get(os.path.join(api,f"league-matches?key={key}&season_id={league_id}").replace("\\","/"))
        data = r.json()
        
        if data['success']:
            data = data["data"]
        else:
            data = []
            send_line_notification("can not get data from league-matches api")
        data = list(map(lambda data: convert_datetime(datetime_f(match_filter(data, league_id))),data))
        # data = list(map(,data))
        # data = list(map(,data))
        return data
    except:
        send_line_notification("can not get data from league-matches api")



def convert_datetime(data):
    
    data["date_unix_thai"] = thai_strftime(datetime.datetime.strptime(data["date_unix"], '%Y-%m-%d').date(), "%e %B %Y")
    return data


def add_match(match, timestamp_now):
    
    # print(match)
    # for k in ["home_ppg","away_ppg","pre_match_home_ppg","pre_match_away_ppg",
    # "pre_match_teamA_overall_ppg","pre_match_teamB_overall_ppg"]:
    #     if not k in match:
    #         match[k] = "0"

    
    defaults = {
    "round_id":match['roundID'], 
    "game_week":match['game_week'], 
    "home_goals":match['homeGoals'],
    "away_goals":match['awayGoals'],  
    "team_a_yellow_cards":max(match['team_a_yellow_cards'],0),
    "team_b_yellow_cards":max(match['team_b_yellow_cards'],0), 
    "team_a_red_cards":max(match['team_a_red_cards'],0), 
    "team_b_red_cards":max(match['team_b_red_cards'],0), 
    "stadium_name":match['stadium_name'], 
    "team_a_dangerous_attacks":max(match['team_a_dangerous_attacks'],0), 
    "team_b_dangerous_attacks":max(match['team_b_dangerous_attacks'],0), 
    "team_a_attacks":max(match['team_a_attacks'],0),
    "team_b_attacks":max(match['team_b_attacks'],0), 
    "team_a_xg":max(match['team_a_xg'],0), 
    "team_b_xg":max(match['team_b_xg'],0), 
    "team_a_penalties_won":max(match['team_a_penalties_won'],0), 
    "team_b_penalties_won":max(match['team_b_penalties_won'],0),
    "team_a_penalty_goals":max(match['team_a_penalty_goals'],0), 
    "team_b_penalty_goals":max(match['team_b_penalty_goals'],0), 
    "team_a_penalty_missed":max(match['team_a_penalty_missed'],0), 
    "team_b_penalty_missed":max(match['team_b_penalty_missed'],0),
    "team_a_throwins":max(match['team_a_throwins'],0), 
    "team_b_throwins":max(match['team_b_throwins'],0), 
    "team_a_freekicks":max(match['team_a_freekicks'],0),
    "team_b_freekicks":max(match['team_b_freekicks'],0), 
    "team_a_goalkicks":max(match['team_a_goalkicks'],0),
    "team_b_goalkicks":max(match['team_b_goalkicks'],0),
    "date_unix" : match["date_unix"],
    "date_unix_thai" : match["date_unix_thai"],
    "home_id" : match["homeID"],
    "away_id" : match["awayID"],
    "season" : match["season"],
    "status" : match["status"],
    "home_goal_count" : max(match["homeGoalCount"],0),
    "away_goal_count" : max(match["awayGoalCount"],0),
    "winning_team" : match["winningTeam"],
    "home_name" : match["home_name"],
    "away_name" : match["away_name"],
    "home_image" : match["home_image"].split("/")[-1],
    "away_image" : match["away_image"].split("/")[-1],
    "home_image_url" : "https://cdn.footystats.org/img/" + match["home_image"],
    "away_image_url" : "https://cdn.footystats.org/img/" + match["away_image"],
    "time_unix" : match["time_unix"],
    "date_update" : timestamp_now,
    "home_ppg": max(match["home_ppg"],0),
    "away_ppg": max(match["away_ppg"],0),
    "pre_match_home_ppg": max(match["pre_match_home_ppg"],0),
    "pre_match_away_ppg": max(match["pre_match_away_ppg"],0),
    "pre_match_teamA_overall_ppg": max(match["pre_match_teamA_overall_ppg"],0),
    "pre_match_teamB_overall_ppg": max(match["pre_match_teamB_overall_ppg"],0)
    }


    FootballMatch.objects.update_or_create(
        league_id=match["league_id"],
        match_id=match["id"],
        defaults=defaults
    )
def save_all_matchs(league_id, update = True):
    setting = AdminSetting.objects.first()
    # FootballMatch.objects.all().delete()
    
    # print(data)
    timestamp_now = int(time.time())
    try:
        latest_entry = FootballMatch.objects.filter(league_id = league_id).latest('date_update').date_update
    except:
        latest_entry = 0
    if abs(latest_entry - timestamp_now) > int(setting.time_matches_update*60) \
            or update:
        data = league_match(setting,league_id = league_id)
        # print(data)
        # with ThreadPoolExecutor() as executor:
        #     executor.map(lambda x: add_match(x,timestamp_now), data)
        for x in data:
            add_match(x,timestamp_now)

        

from django.db.models import F


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
            date_unix__lte = date_unix_lte).order_by('league_id', '-time_unix')
    else:
        data = (FootballMatch.objects.filter(
    date_unix__gte=date_unix_gte, 
    date_unix__lte=date_unix_lte, 
    league_id=league.league_id_last) | FootballMatch.objects.filter(
        date_unix__gte=date_unix_gte, 
    date_unix__lte=date_unix_lte, 
    league_id=league.league_id_prev
    )).order_by('-date_unix', '-time_unix')
    league_all= FootballLeague.objects.all().values()
    league_all = [{'name':x['name'],'league_id_last':x['league_id_last'],
    'league_id_prev':x['league_id_prev']} for x in league_all]
    result_dict = {league['league_id_last']: league['name'] for league in league_all}
    result_dict.update({league['league_id_prev']: league['name'] for league in league_all})
    
    data_date = list(data.values())

    

    data_date = [list(g) for k, g in groupby(data_date, key=itemgetter('date_unix'))]

    
    data_league = list(data.values())
    data_league = [{**x, **{"name": result_dict[x['league_id']]}} for x in data_league]

    data_league = [list(g) for k, g in groupby(data_league, key=itemgetter('name'))]
    return data_date, league,data_league
