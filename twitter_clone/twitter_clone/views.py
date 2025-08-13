from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Welcome to my twitter_clone</h1>")
    return render(request, 'layout.html')