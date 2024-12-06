from django.urls import path
from news.views import *

urlpatterns = [
    path('', home),
    path('calculator/', calculator),
    path('clock/', clock),
    path('countdown/', countdown),
    path('weather/', weather),
    path('game/', game),
    path('drawing/', drawing),
    path('currency/', currency),
    path('registration/', registration),
    path('bar/', progress_bar),
    path('quiz/', quiz),
]
