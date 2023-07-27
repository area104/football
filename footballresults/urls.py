from django.urls import path
from footballresults import views
urlpatterns = [
    path('',views.index),
    path('tablestoday',views.tablestoday, {'date': ''}, name='tablestoday'),
    path('tablestoday/<str:date>',views.tablestoday),
    path('tablesleagues',views.tablesleagues,{'league_id': 0}, name='tablesleagues'),
    path('tablesleagues/<int:league_id>',views.tablesleagues, name='tablesleagues'),
    path('about',views.about),
    path('matchdetail',views.matchdetail),
    
]