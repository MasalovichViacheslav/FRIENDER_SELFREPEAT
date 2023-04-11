from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is {now}.</body></html>"
    return HttpResponse(html)

def greeting(request):
    return HttpResponse("Hello, Django!!!")