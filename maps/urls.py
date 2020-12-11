from django.urls import path

from maps.views import showMap

app_name = 'maps'

urlpatterns = [
    path('maps/', showMap, name='map'),
]