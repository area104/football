from pythainlp.util import thai_strftime
from django.shortcuts import render
import datetime
from .modules.get_all_leagues import *
from .modules.get_all_matchs import *
from .modules.get_match_detail import *
from .modules.get_all_teams import *
from .modules.linenotify import *



# ok
def index(request):
    # save_all_leagues(update = True, save_img = False) #1
    all_leagues = get_all_leagues()
    # all_leagues_id = [[x['league_id_last'],x['league_id_prev']] for x in all_leagues]
    # all_leagues_id = sum(all_leagues_id, [])
    # for id in all_leagues_id:
    #     print("ok",id)
    #     save_all_matchs(id, update = True) #3
    #     save_all_teams(season_id = id,save_img = False , update = True) #2

    return render(request,"index.html",{"all_leagues": all_leagues})


def tablestoday(request, date):
    if date == "":
        date = datetime.datetime.today().date().strftime('%Y-%m-%d')
    league_id = 0
    data, league, data2 = get_all_matchs(league_id=league_id, date_unix_gte = date,
                                    date_unix_lte = date)
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    
    date_bf = date - timedelta(1)
    date_af = date + timedelta(1)
    date_th = thai_strftime(date, "%e %B %Y")
    date_bf_th = thai_strftime(date_bf, "%e %B %Y")
    date_af_th = thai_strftime(date_af, "%e %B %Y")
    date = datetime.datetime.strftime(date, '%Y-%m-%d')
    date_bf = datetime.datetime.strftime(date_bf, '%Y-%m-%d')
    date_af = datetime.datetime.strftime(date_af, '%Y-%m-%d')


    return render(request,"tablestoday.html",{"date":date,"date_bf":date_bf,
    "date_af":date_af,"date_th":date_th,"date_bf_th":date_bf_th,
    "date_af_th":date_af_th,"league1":league, "data": data2,"league_id":league_id})


def tablesleagues(request, league_id):
    date_begin = request.GET.get('begin_date', '')
    date_end = request.GET.get('end_date', '')
    
    data, league,data2 = get_all_matchs(league_id, date_unix_gte = date_begin,
                                    date_unix_lte = date_end)

    
    return render(request,"tablesleagues.html",
    {"league1":league, "data": data,"league_id":league_id})


def about(request):
    return render(request,"about.html")




def matchdetail(request, league_id,match_id):
    data = get_matchdetail(league_id,match_id)

    return render(request,"matchdetail.html",data)
