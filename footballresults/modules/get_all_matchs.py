from footballresults.models import FootballMatch, FootballLeague
import os
from django.conf import settings
import json
import datetime
from pythainlp.util import thai_strftime
from operator import itemgetter
from itertools import groupby
from datetime import timedelta

def convert_datetime(date1):
    # Convert the input date string to a datetime object
    input_date = datetime.datetime.strptime(date1.split(" ")[0], "%Y-%m-%d")

    # Format the datetime as Thai date format
    date1 = thai_strftime(input_date, "%e %B %Y")
    return date1


def get_all_matchs(league_id, date_unix_gte = "2022-08-06",date_unix_lte = "2022-09-03"):
    gmt_offset = 7
    

    # Get today's date
    today = datetime.datetime.now()

    # Calculate the date 7 days ago
    seven_days_ago = today - timedelta(days=7+2*365)

    # Format the date as "YYYY-MM-DD"
    formatted_date = seven_days_ago.strftime("%Y-%m-%d")
    if league_id == "0" or league_id == 0 :
        league = {"name": "", "country":""}
    else:
        league = FootballLeague.objects.filter(league_id=str(league_id)).first()
    if date_unix_gte == "":
        date_unix_gte = formatted_date
    if date_unix_lte == "":
        date_unix_lte = today.strftime("%Y-%m-%d")
    if league_id == "0" or league_id == 0 :
        data = FootballMatch.objects.filter(date_unix__gte = date_unix_gte,
            date_unix__lte = date_unix_lte).values('status', 'match_id', 'date_unix', 'time_unix',
            'home_goal_count','away_goal_count','winning_team','home_name','away_name',
            "home_id","away_id","season")
    else:
        data = FootballMatch.objects.filter(date_unix__gte = date_unix_gte,
        date_unix__lte = date_unix_lte,
        league_id=league_id).values('status', 'match_id', 'date_unix', 'time_unix',
        'home_goal_count','away_goal_count','winning_team','home_name','away_name',
        "home_id","away_id","season")
        data = list(data.values('status', 'match_id', 'date_unix', 'time_unix',
        'home_goal_count','away_goal_count','winning_team','home_name','away_name',
        "home_id","away_id","season"))
    data1 = []
    for x in data:
        x['date_unix']=convert_datetime(x['date_unix'])
        x['time_unix']=":".join(x['time_unix'].split(":")[:2]) + " น."
        data1.append(x)
    print(data1)

    data1.sort(key=itemgetter('date_unix'))

    data = [list(g) for k, g in groupby(data, key=itemgetter('date_unix'))]
    return data, league

def save_all_matchs(gmt_offset,league_id):
    count, _  = FootballMatch.objects.all().delete()
    file_path = os.path.join(settings.BASE_DIR, 'footballresults', 'data', 'league-matches-7704.json')
    with open(file_path) as f:
        data = json.load(f)["data"]

    key1 = ['id',  "date_unix", 'homeID', 'awayID', 'season', 'status','homeGoalCount', 'awayGoalCount', 'totalGoalCount',
    'winningTeam','home_image', 'home_name', 'away_image', 'away_name']
    for i in range(len(data)):
        data1 = {}
        for k in key1:
            data1[k] = data[i][k]
            

            if k in ["home_image", "away_image"]:
                data1[k] = "https://cdn.footystats.org/img/"+data1[k]
        data1["date_unix"] =  datetime.datetime.utcfromtimestamp(data1["date_unix"]) + \
                                datetime.timedelta(hours=gmt_offset)

        # Format the datetime as a string
        data1["date_unix"] = data1["date_unix"].strftime('%Y-%m-%d %H:%M:%S')
        data1["time_unix"] = data1["date_unix"].split(" ")[1]
        data1["date_unix"] = data1["date_unix"].split(" ")[0]
        


        data[i] = data1.copy()
    
    count, _ = FootballMatch.objects.all().delete()
    for match in data:
        match = FootballMatch(match_id = match["id"],date_unix = match["date_unix"],home_id = match["homeID"],
        away_id = match["awayID"],season = match["season"],status = match["status"],
        home_goal_count = match["homeGoalCount"],
        away_goal_count = match["awayGoalCount"],winning_team = match["winningTeam"],
        home_name = match["home_name"],away_name = match["away_name"],
        home_image = match["home_image"].split("/")[-1],
        away_image = match["away_image"].split("/")[-1],
        league_id = league_id,time_unix = match["time_unix"])

    #     
        match.save()