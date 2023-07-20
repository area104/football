from django.urls import path
from footballresults import views
urlpatterns = [
    path('',views.index),
    path('about',views.about),
]