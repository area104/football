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
from .modules.get_all_leagues import *
from .modules.get_all_matchs import *
from .modules.get_match_detail import *
from .modules.get_all_teams import *
from pythainlp.util import thai_strftime
# ok
def index(request):
    # print(save_all_teams(season_id = 8777,save_img = True))
    save_all_leagues()
    all_leagues = get_all_leagues()

    return render(request,"index.html",{"all_leagues":all_leagues})

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
    # print(data2)
    

    return render(request,"tablestoday.html",{"date":date,"date_bf":date_bf,
    "date_af":date_af,"date_th":date_th,"date_bf_th":date_bf_th,
    "date_af_th":date_af_th,"league1":league, "data": data2,"league_id":league_id})


def tablesleagues(request, league_id):
    date_begin = request.GET.get('begin_date', '')
    date_end = request.GET.get('end_date', '')
    
    l1 = FootballLeague.objects.filter(league_id_last=league_id).first()
    save_all_matchs(league_id = l1.league_id_prev)
    save_all_matchs(league_id = league_id)
    data, league,data2 = get_all_matchs(league_id, date_unix_gte = date_begin,
                                    date_unix_lte = date_end)

    
    return render(request,"tablesleagues.html",
    {"league1":league, "data": data,"league_id":league_id})


def about(request):
    return render(request,"about.html")

def matchdetail(request, league_id,match_id):
    data = get_match_detail(league_id, match_id)

    return render(request,"matchdetail.html",{"data":data})

    