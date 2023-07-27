from django.shortcuts import render
from django.http import HttpResponse
# Import the model
from footballresults.models import FootballMatch, FootballLeague
import json
from django.conf import settings
import os
import requests
import time
# To retrieve all records from the collection:
import datetime
from pythainlp.util import thai_strftime
from itertools import groupby
from operator import itemgetter

# Create your views here.
def index(request):
    # home_team = "VV"
    # home_score = "5"
    # count, _  = FootballMatch.objects.all().delete()
    # match.save()


    # all_matches = FootballMatch.objects.all()
    # users = FootballMatch.objects.filter(home_team='B')

    # file_path = os.path.join(settings.BASE_DIR, 'footballresults', 'data', 'league-list.json')
    # with open(file_path) as f:
    #     data = json.load(f)["data"]
    # data = [{"name": league["league_name"], "country": league["country"], 
    # "image": league["image"],"league_year": league["season"][-1]["year"],
    # "league_id": league["season"][-1]["id"]} for league in data if "image" in league]
    # print(data)
    # count, _ = FootballLeague.objects.all().delete()
    # for league in data:
    #     match = FootballLeague(name=league["name"], country=league["country"],
    #     image = league["image"].split("/")[-1], league_id = league["league_id"], league_year = league["league_year"])
    #     match.save()
    data = FootballLeague.objects.all()[:20]
    # i = 0
    # for record in data:
    #     i+=1
    #     if i<1380:
    #         continue
    #     time.sleep(0.1)
    #     url = "https://cdn.footystats.org/img/competitions/"+record.image
    #     r = requests.get(url)
    #     if r.status_code == 200:
    #         image_data = r.content
    #         static_folder_path = './footballresults/static/images/leagues'
    #         os.makedirs(static_folder_path, exist_ok=True)
    #         file_name = url.split("/")[-1]
    #         file_path = os.path.join(static_folder_path, file_name)
    #         with open(file_path, 'wb') as f:
    #             f.write(image_data)



    return render(request,"index.html",{"users":"all_matches","data":data})

def tablestoday(request):
    return render(request,"tablestoday.html")

def add_data_matches(gmt_offset,league_id):
    file_path = os.path.join(settings.BASE_DIR, 'footballresults', 'data', 'league-matches-7704.json')
    with open(file_path) as f:
        data = json.load(f)["data"]
    # 'homeGoals', 'awayGoals', 

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

def convert_datetime(date1):
    # Convert the input date string to a datetime object
    input_date = datetime.datetime.strptime(date1.split(" ")[0], "%Y-%m-%d")

    # Format the datetime as Thai date format
    date1 = thai_strftime(input_date, "%e %B %Y")
    return date1
def tablesleagues(request, league_id):
    your_param = request.GET.get('a', '0')
    gmt_offset = 7

    # add_data_matches(gmt_offset,league_id)
    league = FootballLeague.objects.filter(league_id=str(league_id)).first()
    # data = FootballMatch.objects.all()[:20]
    data = FootballMatch.objects.filter(date_unix__gte = "2022-08-06",date_unix__lte = "2022-09-03",
    league_id=league_id).values('status', 'match_id', 'date_unix', 'time_unix',
    'home_goal_count','away_goal_count','winning_team','home_name','away_name',
    "home_id","away_id","season")
    data = list(data.values('status', 'match_id', 'date_unix', 'time_unix',
    'home_goal_count','away_goal_count','winning_team','home_name','away_name',
    "home_id","away_id","season"))
    data1 = []
    for x in data:
        x['date_unix']=convert_datetime(x['date_unix'])
        x['time_unix']=":".join(x['time_unix'].split(":")[:2])
        data1.append(x)
    print(data1)

    data1.sort(key=itemgetter('date_unix'))

    data = [list(g) for k, g in groupby(data, key=itemgetter('date_unix'))]
    print(data)

    return render(request,"tablesleagues.html",
    {"league1":league, "data": data,"league_id":league_id,"a":your_param})


def about(request):
    return render(request,"about.html")

def matchdetail(request):
    return render(request,"matchdetail.html")

    