from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    a = 5
    return render(request,"index.html",{"a":a,"b":6})

def about(request):
    return render(request,"about.html")

