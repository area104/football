from footballresults.models import FootballMatch, FootballLeague
from app_admins.models import AdminSetting
import os
from django.conf import settings
import json
import time
import requests
import datetime
from glob import glob
import datetime
from ..modules.read_api import *

from concurrent.futures import ThreadPoolExecutor
from functools import partial

def save_image_from_url(url, save_path):
    os.makedirs(save_path, exist_ok=True)
    
    filename = url.split("/")[-1]  # gets 'slovakia-i-liga-women.png'
    save_path = os.path.join(save_path, filename)  # path where image will be saved
    if len(glob(save_path))==0:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
    return filename
                

def get_all_leagues():
    all_leagues = FootballLeague.objects.all()
    all_leagues = list(all_leagues.values())
    return all_leagues

def save_match(league, timestamp_now):
    if len(league["season"]) > 1:
        league_id_prev = league["season"][-2]["id"]
    else:
        league_id_prev = 0
    match = FootballLeague(
        name=league["name"], 
        country=league["country"],
        image=league["image"].split("/")[-1], 
        league_id_prev=league_id_prev,
        league_id_last=league["season"][-1]["id"],
        date_update=timestamp_now
    )
    
    match.save()
    return 0



def save_all_leagues(update = False):
    
    
    setting = AdminSetting.objects.first()
    
    league_list, api, key = setting.league_list, setting.web_api, setting.api_key
    league_list = [x.strip().replace("-","").replace("  "," ") for x in league_list.split("\n")]

    timestamp_now = int(time.time())
    try:
        latest_entry = FootballLeague.objects.latest('date_update').date_update
    except:
        latest_entry = 0

    if abs(latest_entry - timestamp_now) > int(setting.time_league_update*60):
        response = requests.get(f"{api}league-list?key={key}")
        data = response.json()
        if data['success']:
            data = data["data"]
        else:
            data = []
            return data

        data = list(filter(lambda x: x['name'] in league_list, data))

        file_path_img = os.path.join(settings.BASE_DIR, 'footballresults', 'static', 'images','leagues')

        

        with ThreadPoolExecutor() as executor:
            func = partial(save_image_from_url, save_path=file_path_img)
            executor.map(func, [league["image"] for league in data])
        
        count, _ = FootballLeague.objects.all().delete()

        with ThreadPoolExecutor() as executor:
            executor.map(lambda x: save_match(x, timestamp_now), data)


