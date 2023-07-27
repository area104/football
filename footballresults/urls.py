from django.urls import path
from footballresults import views
urlpatterns = [
    path('',views.index),
    path('tablestoday',views.tablestoday),
    path('tablesleagues/<int:league_id>',views.tablesleagues, name='tablesleagues'),
    path('about',views.about),
    path('matchdetail',views.matchdetail),
    
]