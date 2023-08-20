from django.urls import path
from footballresults import views
urlpatterns = [
    path('',views.index),
    path('tablestoday',views.tablestoday, {'date': ''}, name='tablestoday'),
    path('tablestoday/<str:date>',views.tablestoday),
    path('tablesleagues',views.tablesleagues,
        {'league_id': 0}, 
        name='tablesleagues'),
    path('tablesleagues/<int:league_id>', views.tablesleagues,
        name='tablesleagues'),
    
    path('about',views.about),
    path('matchdetail/<int:league_id>/<int:match_id>',views.matchdetail),
    # path('admin_login',views.admin_login),
    # path('admin_users',views.admin_user),
    # path('admin_setting',views.admin_setting),
    # path('admin_register',views.admin_register),

    
]