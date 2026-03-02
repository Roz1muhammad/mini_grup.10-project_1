from django.urls import path
from core.views.home import *

urlpatterns = [
    path('', home_view),
]
