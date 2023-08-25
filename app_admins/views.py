from footballresults.models import FootballLeague, FootballMatch, FootballTeams
from django.shortcuts import render, redirect
from .forms import RegisterForm, AdminSettingsForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse
from app_admins.models import AdminSetting
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from footballresults.models import FootballMatch, FootballLeague, FootballTeams
from footballresults.modules.save_all_data import *
import pandas as pd

def delete_user(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('users')


def delete_league(request, league_id):
    if not request.user.is_authenticated:
        return redirect('login')
    league_id_last = FootballLeague.objects.filter(league_id_last = league_id).first().league_id_last
    league_id_prev = FootballLeague.objects.filter(league_id_last = league_id).first().league_id_prev
    FootballTeams.objects.filter(season_id = league_id_last).delete()
    FootballTeams.objects.filter(season_id = league_id_prev).delete()
    FootballMatch.objects.filter(league_id = league_id_last).delete()
    FootballMatch.objects.filter(league_id = league_id_prev).delete()
    FootballLeague.objects.filter(league_id_last = league_id).delete()
    return redirect('data')

def delete_team(request, league_id):
    if not request.user.is_authenticated:
        return redirect('login')
    FootballTeams.objects.filter(season_id = league_id).delete()
    return redirect('data')

def delete_match(request, league_id):
    if not request.user.is_authenticated:
        return redirect('login')
    FootballMatch.objects.filter(league_id = league_id).delete()
    return redirect('data')

class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('setting')
        return super().get(request, *args, **kwargs)


# Create your views here.
def register(request: HttpRequest):
    if request.method == "POST":
        try:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                # login(request, user)
                return redirect('users')
            
        except:
            return redirect('users')
    else:
        if not request.user.is_authenticated:
            return redirect('login')
        form = RegisterForm()
    
    return render(request, "app_users/register.html",
    {"form": form})

from django.http import JsonResponse

def updatedata(request):
    save_all_data(update=False, delete=False)
    data = {"message": "Data updated successfully"}
    return JsonResponse(data)

def setting(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        
        form = AdminSettingsForm(request.POST)
        if form.is_valid():
            # Create an AdminSetting object but don't save it yet
            AdminSetting.objects.all().delete()
            admin_setting = AdminSetting(
                web_api =  form.cleaned_data['web_api'],
                date_update = 0,
                userid = 1,
                api_key=form.cleaned_data['api_key'],
                line_api=form.cleaned_data['line_api_key'],
                # ... add other fields
                time_league_update=form.cleaned_data['duration_for_get_leagues_data'],
                time_time_update=form.cleaned_data['duration_for_get_teams_data'],
                time_matches_update=form.cleaned_data['duration_for_get_matches_data'],
                # If you want to add the league name to the JSONField, you can do:
                league_list=form.cleaned_data['add_league_name'],
                user_get_api = form.cleaned_data['user_get_api'],

            )
            admin_setting.save()
        save_all_data(update = True, delete = True)
        return redirect('data')
    else:
        admin_setting = AdminSetting.objects.first()
        if admin_setting:
            form_data = {
                'web_api': admin_setting.web_api,
                'api_key': admin_setting.api_key,
                'line_api_key': admin_setting.line_api,
                'add_league_name': admin_setting.league_list,
                'duration_for_get_leagues_data': admin_setting.time_league_update,
                'duration_for_get_teams_data': admin_setting.time_time_update,
                'duration_for_get_matches_data': admin_setting.time_matches_update,
                'user_get_api': admin_setting.user_get_api
            }
            form = AdminSettingsForm(initial=form_data)
        else:
            form = AdminSettingsForm()


    return render(request,"setting.html",{"form": form,"user":request.user})

def users(request):
    if not request.user.is_authenticated:
        return redirect('login')

    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


import datetime
import pytz
def date_time_thai(timestamp = 1692667126):


    # Convert timestamp to a datetime object
    utc_dt = datetime.datetime.utcfromtimestamp(timestamp)

    # Define the timezone for Thailand
    thai_timezone = pytz.timezone('Asia/Bangkok')

    # Convert UTC datetime to Thai local time
    thai_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(thai_timezone)

    # Format the Thai local time as a string
    thai_datetime_str = thai_dt.strftime('%Y-%m-%d %H:%M:%S')

    return thai_datetime_str

def datasetting(request):
    if not request.user.is_authenticated:
        return redirect('login')
    step = 0
    try:
        
        data_league = FootballLeague.objects.values(
            "name",
            "country",
            "league_id_last",
            "league_id_prev","date_update").distinct()
        
        data_match = FootballMatch.objects.values("league_id",
            "season","date_update").distinct()

        data_team = FootballTeams.objects.values("season_id",
        "season","date_update").distinct()
        data_match = list(data_match)
        data_league = list(data_league)
        data_team = list(data_team)
        
        df_league1 = pd.DataFrame(data_league)
        df_match1 = pd.DataFrame(data_match)
        df_season1 = pd.DataFrame(data_team)
        

        df_league1 = pd.concat([df_league1.drop(columns = "league_id_prev") \
        .rename(columns = {"league_id_last":"league_id"}),
            df_league1.drop(columns = "league_id_last").rename(columns = {"league_id_prev":"league_id"})],
            axis = 0)
        df_league = pd.merge(pd.DataFrame(data_league).drop(columns = "league_id_prev") \
        .rename(columns = {"league_id_last":"league_id"}), df_season1[["season_id", "season"]], how = "left", left_on = "league_id",
        right_on = "season_id")
        

        df_league = df_league.sort_values(by = ["name", "season"])
        df_league["date_update"] = df_league["date_update"].apply(date_time_thai)
        
        df_league["season_id"] = df_league["league_id"].apply(int)
        print("abc")
        df_league = df_league.to_dict(orient='records')
        step = 1

        df_season = pd.merge(df_league1[["name", "country", "league_id"]], 
                df_season1, how = "right", left_on = "league_id",
        right_on = "season_id")
        
        df_season = df_season.sort_values(by = ["name", "season"])
        df_season["date_update"] = df_season["date_update"].apply(date_time_thai)
        df_season["season_id"] = df_season["season_id"].apply(int)
        df_season = df_season.to_dict(orient='records')
        step = 2

        df_match = pd.merge(df_league1[["name", "country", "league_id"]], 
                df_match1, how = "right", on = "league_id").rename(columns = {"league_id": "season_id"})

        df_match = df_match.sort_values(by = ["name", "season"])
        df_match["date_update"] = df_match["date_update"].apply(date_time_thai)
        df_match["season_id"] = df_match["season_id"].apply(int)
        df_match = df_match.to_dict(orient='records')
        step = 3


        
        
        

            
        return render(request, 'datasetting.html',{"data_league":df_league,
        "data_match":df_match, "data_team":df_season})
    except:
        print("xxxxx")
        if step == 0:
            print("xxxxx1")
            return render(request, 'datasetting.html',{"data_league":[],
            "data_match":[], "data_team":[]})
        elif step == 1:
            print("xxxxx2")
            return render(request, 'datasetting.html',{"data_league":df_league,
            "data_match":[], "data_team":df_season})
        elif step == 2:
            print("xxxxx3")
            return render(request, 'datasetting.html',{"data_league":df_league,
            "data_match":[], "data_team":[]})