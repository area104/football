from footballresults.models import FootballMatch, FootballLeague
import os
from django.conf import settings
import json
import time
import requests
import datetime
from glob import glob
import datetime
from ..modules.read_api import *
def save_image_from_url(url, save_path):
    os.makedirs(save_path, exist_ok=True)
    
    filename = url.split("/")[-1]  # gets 'slovakia-i-liga-women.png'
    save_path = os.path.join(save_path, filename)  # path where image will be saved
    if len(glob(save_path))==0:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)



def get_all_leagues():
    all_leagues = FootballLeague.objects.all()
    all_leagues = list(all_leagues.values())
    return all_leagues
    
def save_all_leagues():

    league_list, api, key = read_api()
    

    timestamp_now = int(time.time())
    try:
        latest_entry = FootballLeague.objects.latest('date_update').date_update
    except:
        latest_entry = 0
    if abs(latest_entry - timestamp_now) > 60*60*24*30:
        response = requests.get(f"{api}league-list?key={key}")
        data = response.json()
        if data['success']:
            data = data["data"]
        else:
            data = []
        data = [x for x in data if x["name"] in league_list]


        file_path_img = os.path.join(settings.BASE_DIR, 'footballresults', 'static', 'images','leagues')
        for league in data:
            save_image_from_url(league["image"], file_path_img)
            time.sleep(0.2)

        count, _ = FootballLeague.objects.all().delete()

        for league in data:
            if len(league["season"]) > 1:
                league_id_prev = league["season"][-2]["id"]
            else:
                league_id_prev = 0
            match = FootballLeague(name=league["name"], 
            country=league["country"],
            image = league["image"].split("/")[-1], 
            league_id_prev = league_id_prev,
            league_id_last = league["season"][-1]["id"],
            date_update = timestamp_now)
            match.save()

