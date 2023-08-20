
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

def delete_user(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('users')

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
                login(request, user)
                return redirect('setting')
        except:
            return redirect('setting')
    else:
        if not request.user.is_authenticated:
            return redirect('register')
        form = RegisterForm()
    
    return render(request, "app_users/register.html",
    {"form": form})

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
                league_list=form.cleaned_data['add_league_name']
            )
            admin_setting.save()
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

def datasetting(request):
    if not request.user.is_authenticated:
        return redirect('login')