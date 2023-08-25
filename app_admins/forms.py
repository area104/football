# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    # note = forms.CharField(widget=forms.TextInput())
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields # + ('note',)

class AdminSettingsForm(forms.Form):
    web_api = forms.CharField(label='API url', widget=forms.TextInput(attrs={'class': 'form-control'}))
    api_key = forms.CharField(label='API Key', widget=forms.TextInput(attrs={'class': 'form-control'}))
    line_api_key = forms.CharField(label='Line API Key', widget=forms.TextInput(attrs={'class': 'form-control'}))
    add_league_name = forms.CharField(
                        label='Add League Name',
                        widget=forms.Textarea(attrs={'class': 'form-control'})
                    )
    duration_for_get_leagues_data = forms.IntegerField(label='Duration for Get Leagues Data (minutes)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    duration_for_get_teams_data = forms.IntegerField(label='Duration for Get Teams Data (minutes)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    duration_for_get_matches_data = forms.IntegerField(label='Duration for Get Matches Data (minutes)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    user_get_api = forms.IntegerField(label='User get API', widget=forms.NumberInput(attrs={'class': 'form-control'}))

