from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is {now}.</body></html>"
    return HttpResponse(html)

def greeting(request):
    return HttpResponse("Hello, Django!!!")

def app_creation_year(request, year):
    return HttpResponse(f'This APP was created in {year}')

def app_creation_date(request, app_date):
    return HttpResponse(f'This APP was created on {app_date}')

def site_creation_date(request):
    return HttpResponse(f'This site was created on 2023-04-12')



