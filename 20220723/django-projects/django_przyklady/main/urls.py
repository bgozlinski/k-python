
from django.urls import path

from main.views import homepage, greetings

urlpatterns = [
    path('', homepage),
    path('greetings/', greetings),
]