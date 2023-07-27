from footballresults.models import FootballMatch, FootballLeague
import os
from django.conf import settings
import json
import time
import requests

def get_all_leagues():
    pass
    
def save_all_leagues():
    count, _  = FootballMatch.objects.all().delete()
    file_path = os.path.join(settings.BASE_DIR, 'footballresults', 'data', 'league-list.json')
    with open(file_path) as f:
        data = json.load(f)["data"]
    data = [{"name": league["league_name"], "country": league["country"], 
    "image": league["image"],"league_year": league["season"][-1]["year"],
    "league_id": league["season"][-1]["id"]} for league in data if "image" in league]
    print(data)
    count, _ = FootballLeague.objects.all().delete()
    for league in data:
        match = FootballLeague(name=league["name"], country=league["country"],
        image = league["image"].split("/")[-1], league_id = league["league_id"], league_year = league["league_year"])
        match.save()


def save_img_leagues():
    time.sleep(1)
    data = FootballLeague.objects.all()
    i = 0
    for record in data:
        i+=1
        time.sleep(0.1)
        url = "https://cdn.footystats.org/img/competitions/"+record.image
        r = requests.get(url)
        if r.status_code == 200:
            image_data = r.content
            static_folder_path = './footballresults/static/images/leagues'
            os.makedirs(static_folder_path, exist_ok=True)
            file_name = url.split("/")[-1]
            file_path = os.path.join(static_folder_path, file_name)
            with open(file_path, 'wb') as f:
                f.write(image_data)