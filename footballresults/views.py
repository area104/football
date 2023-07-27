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

# ok
def index(request):
    all_leagues = FootballLeague.objects.all()[:5]
    return render(request,"index.html",{"all_leagues":all_leagues})

def tablestoday(request, date):
    return render(request,"tablestoday.html")

def tablesleagues(request, league_id):
    date_begin = request.GET.get('date_begin', '')
    date_end = request.GET.get('date_end', '')
    print("xx",date_begin,date_end)
    # save_all_matchs(gmt_offset = 7,league_id = league_id)
    data, league = get_all_matchs(league_id,date_unix_gte = date_begin,date_unix_lte = date_end)
    

    return render(request,"tablesleagues.html",
    {"league1":league, "data": data,"league_id":league_id})


def about(request):
    return render(request,"about.html")

def matchdetail(request):
    return render(request,"matchdetail.html")

    