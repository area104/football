from django.urls import path, include
from app_admins import views
from .views import CustomLoginView
from app_admins import views

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),  # Your custom login view
    path("register", views.register, name="register"),
    path("setting", views.setting, name="setting"),
    path("users", views.users, name="users"),
    path("data", views.datasetting, name="data"),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path("", include("django.contrib.auth.urls")),  # This includes all the other authentication views
path("", CustomLoginView.as_view(), name='login'),
]