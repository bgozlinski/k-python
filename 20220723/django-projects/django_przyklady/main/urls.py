
from django.urls import path

from main.views import homepage, greetings

urlpatterns = [
    path('', homepage, name='home_page'),
    path('greetings/', greetings),
]