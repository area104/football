from django.urls import path, include
from app_admins import views
from .views import CustomLoginView
from app_admins import views

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),  # Your custom login view
    path("register", views.register, name="register"),
    path("updatedata", views.updatedata, name="updatedata"),
    path("setting", views.setting, name="setting"),
    path("users", views.users, name="users"),
    path("data", views.datasetting, name="data"),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete_league/<int:league_id>/', views.delete_league, name='delete_league'),
    path('delete_team/<int:league_id>/', views.delete_team, name='delete_team'),
    path('delete_match/<int:league_id>/', views.delete_match, name='delete_match'),
    path("", include("django.contrib.auth.urls")),  # This includes all the other authentication views
path("", CustomLoginView.as_view(), name='login'),
]