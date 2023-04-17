from django.shortcuts import render
from django.http import HttpResponse
import datetime


def main_page(request):
    return render(request, 'main.html')


def users(request):
    user_list = {
        'Andrei': [25, 'male', 'Minsk'],
        'Dmitri': [27, 'male', 'Minsk'],
        'Pavel': [23, 'male', 'Orsha'],
        'Olga': [24, 'female', 'Minsk'],
        'Yulia': [22, 'female', 'Minsk'],
        'Anna': [21, 'female', 'Vitebsk']
    }
    return render(request, 'users.html', context={'users': user_list})

def places(request):
    return render(request, 'places.html')

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = f"<html><body>It is {now}.</body></html>"
#     return HttpResponse(html)

# def greeting(request):
#     return HttpResponse("Hello, Django!!!")

# def app_creation_year(request, year):
#     return HttpResponse(f'This APP was created in {year}')

# def app_creation_date(request, app_date):
#     return HttpResponse(f'This APP was created on {app_date}')

# def site_creation_date(request):
#     return HttpResponse(f'This site was created on 2023-04-12')

# def show_example(request):
#     return render(request, "example.html", {'first_name': 'John', 'last_name': 'Doe'})



