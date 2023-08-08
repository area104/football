import os
import json
from django.conf import settings
def read_api():
    file_league_list = os.path.join(settings.BASE_DIR, 'footballresults', 'setting', 'leagues_list.json')
    with open(file_league_list,"r") as f:
        league_list = json.load(f)

    file_apikey = os.path.join(settings.BASE_DIR, 'footballresults', 'setting', 'apikeys.json')
    with open(file_apikey,"r") as f:
        apikey = json.load(f)
        api = apikey["api"]
        key = apikey["api_key"]
    print("okkkk")
    return league_list, api, key