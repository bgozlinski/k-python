from django.urls import path
from books.views import listview


urlpatterns = [
    path('', listview),
]