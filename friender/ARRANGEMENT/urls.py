from django.urls import path, re_path
from .views import *

urlpatterns = [
    # path('time/', current_datetime),
    # path('greeting/', greeting),
    # path('<int:year>/', app_creation_year),
    # path('<slug:app_date>/', app_creation_date),
    # re_path(r'\d{4}.\d{2}.\d{2}', site_creation_date),
    # path('example/', show_example),
    path('main/', main_page, name="HOME_PAGE"),
    path('users/', users, name="USERS_PAGE"),
    path('places/', places, name="PLACES_PAGE"),
]