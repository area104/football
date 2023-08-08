from footballresults.models import FootballMatch, FootballLeague, FootballTeams
import os
from django.conf import settings
import json
import time
import requests
import datetime
from glob import glob
def save_image_from_url(url, save_path):
    os.makedirs(save_path, exist_ok=True)
    
    filename = url.split("/")[-1]  # gets 'slovakia-i-liga-women.png'
    save_path = os.path.join(save_path, filename)  # path where image will be saved
    if len(glob(save_path))==0:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)



def league_team_filter(data,season_id):
    data = {key: data[key] for key in ['id', 'name', 'cleanName',
                                     'english_name', 'shortHand',
                'country', \
                'founded', 'image', 'season', 'table_position', \
                'performance_rank', 'risk', 'season_format',
                                     'competition_id',
                'full_name',"stats"]}
    data["stats"] = {key: data["stats"][key] for key in {'drawPercentage_away', 'drawPercentage_home', 'drawPercentage_overall',
 'leaguePosition_away', 'leaguePosition_home', 'leaguePosition_overall',
 'losePercentage_away', 'losePercentage_home', 'losePercentage_overall',
 'name_th', 'prediction_risk', 'seasonConcededNum_away', 'seasonConcededNum_home',
 'seasonConcededNum_overall', 'seasonDrawsNum_away', 'seasonDrawsNum_home',
 'seasonDrawsNum_overall', 'seasonFTS_away', 'seasonFTS_home', 'seasonFTS_overall',
 'seasonGoalDifference_away', 'seasonGoalDifference_home', 'seasonGoalDifference_overall',
 'seasonGoalsTotal_away', 'seasonGoalsTotal_home', 'seasonGoalsTotal_overall',
  'seasonLossesNum_away', 'seasonLossesNum_home',
 'seasonLossesNum_overall', 'seasonMatchesPlayed_away', 'seasonMatchesPlayed_home',
 'seasonMatchesPlayed_overall', 'seasonScoredNum_away', 'seasonScoredNum_home',
 'seasonScoredNum_overall', 'seasonWinsNum_away', 'seasonWinsNum_home',
 'seasonWinsNum_overall', 'suspended_matches', 'winPercentage_away',
 'winPercentage_home', 'winPercentage_overall'}}
    data["season_id"] = season_id
    for x in data["stats"]:
        data["stats_"+x]=data["stats"][x]
    del data["stats"]
    return data





def get_all_teams():
    pass

def save_all_teams(season_id = 8777,save_img = False):

    file_path_img = os.path.join(settings.BASE_DIR, 'footballresults', 'static', 'images','teams')
    file_path = os.path.join(settings.BASE_DIR, 'footballresults', 'data', 'league-teams.json')
    with open(file_path,"r") as f:
        data = json.load(f)
    if data['success']:
        data = data["data"]
    else:
        data = []


    data = list(map(lambda x: league_team_filter(x, season_id),data))
    print(data)
    if save_img:
        for league in data:
            save_image_from_url(league["image"], file_path_img)
            time.sleep(0.1)


    count, _ = FootballTeams.objects.all().delete()

    for team in data:
        
        match = FootballTeams(
                id = team["id"],
name = team["name"],
cleanName = team["cleanName"],
english_name = team["english_name"],
 shortHand = team["shortHand"],
 country = team["country"],
 founded = team["founded"],
 image = team["image"].split("/")[-1],
 season = team["season"],
 table_position = team["table_position"],
 performance_rank = team["performance_rank"],
 risk = team["risk"],
 season_format = team["season_format"],
 competition_id = team["competition_id"],
 full_name = team["full_name"],
 season_id = season_id,
 stats_seasonMatchesPlayed_away = team["stats_seasonMatchesPlayed_away"],
 stats_seasonWinsNum_away = team["stats_seasonWinsNum_away"],
 stats_seasonFTS_away = team["stats_seasonFTS_away"],
 stats_seasonDrawsNum_home = team["stats_seasonDrawsNum_home"],
 stats_losePercentage_overall = team["stats_losePercentage_overall"],
 stats_losePercentage_away = team["stats_losePercentage_away"],
 stats_leaguePosition_away = team["stats_leaguePosition_away"],
 stats_prediction_risk = team["stats_prediction_risk"],
 stats_leaguePosition_home = team["stats_leaguePosition_home"],
 stats_seasonConcededNum_overall = team["stats_seasonConcededNum_overall"],
 stats_seasonFTS_home = team["stats_seasonFTS_home"],
 stats_seasonFTS_overall = team["stats_seasonFTS_overall"],
 stats_seasonLossesNum_overall = team["stats_seasonLossesNum_overall"],
 stats_seasonScoredNum_away = team["stats_seasonScoredNum_away"],
 stats_seasonMatchesPlayed_overall = team["stats_seasonMatchesPlayed_overall"],
 stats_seasonWinsNum_home = team["stats_seasonWinsNum_home"],
 stats_seasonGoalDifference_overall = team["stats_seasonGoalDifference_overall"],
 stats_name_th  = team["stats_name_th"],
 stats_leaguePosition_overall = team["stats_leaguePosition_overall"],
 stats_suspended_matches = team["stats_suspended_matches"],
 stats_drawPercentage_overall = team["stats_drawPercentage_overall"],
 stats_seasonGoalDifference_away = team["stats_seasonGoalDifference_away"],
 stats_seasonConcededNum_away = team["stats_seasonConcededNum_away"],
 stats_seasonGoalsTotal_away = team["stats_seasonGoalsTotal_away"],
 stats_seasonGoalsTotal_home = team["stats_seasonGoalsTotal_home"],
 stats_seasonWinsNum_overall = team["stats_seasonWinsNum_overall"],
 stats_seasonLossesNum_home = team["stats_seasonLossesNum_home"],
 stats_seasonDrawsNum_away = team["stats_seasonDrawsNum_away"],
 stats_losePercentage_home = team["stats_losePercentage_home"],
 stats_seasonGoalsTotal_overall = team["stats_seasonGoalsTotal_overall"],
 stats_winPercentage_home = team["stats_winPercentage_home"],
 stats_drawPercentage_away = team["stats_drawPercentage_away"],
 stats_winPercentage_overall = team["stats_winPercentage_overall"],
 stats_drawPercentage_home = team["stats_drawPercentage_home"],
 stats_seasonScoredNum_overall = team["stats_seasonScoredNum_overall"],
 stats_seasonLossesNum_away = team["stats_seasonLossesNum_away"],
 stats_seasonDrawsNum_overall = team["stats_seasonDrawsNum_overall"],
 stats_seasonGoalDifference_home = team["stats_seasonGoalDifference_home"],
 stats_seasonMatchesPlayed_home = team["stats_seasonMatchesPlayed_home"],
 stats_winPercentage_away = team["stats_winPercentage_away"],
 stats_seasonScoredNum_home = team["stats_seasonScoredNum_home"],
 stats_seasonConcededNum_home = team["stats_seasonConcededNum_home"])

        match.save()

