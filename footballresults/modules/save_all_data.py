from .get_all_leagues import *
from .get_all_matchs import *
from .get_all_teams import *
from footballresults.models import FootballMatch, FootballLeague, FootballTeams

def save_all_data(update = False, delete = False, data = "", id = ""):
    if data == "":
        if delete:
            FootballLeague.objects.all().delete()
            FootballMatch.objects.all().delete()
            FootballTeams.objects.all().delete()

        save_all_leagues(update = update, save_img = False)
        all_leagues = get_all_leagues()
        all_leagues_id = [x['league_id_last'] for x in all_leagues]
        # all_leagues_id = [[x['league_id_last'],x['league_id_prev']] for x in all_leagues]
        # all_leagues_id = sum(all_leagues_id, [])
        for id in all_leagues_id:
            save_all_matchs(id, update = update)
            save_all_teams(season_id = id,save_img = False , update = update)
    elif data == "league":
        if delete:
            FootballLeague.objects.all().delete()
        save_all_leagues(update = update, save_img = False)
    elif data == "team":
        if delete:
            FootballTeams.objects.all().delete()
        save_all_teams(season_id = id,save_img = False , update = update)
    elif data == "match":
        if delete:
            FootballMatch.objects.all().delete()
        if id != 0:
            save_all_matchs(id, update = update)
        else:
            all_leagues = get_all_leagues()
            all_leagues_id = [x['league_id_last'] for x in all_leagues]
            for id in all_leagues_id:
                save_all_matchs(id, update = update)

        


        
