from django.urls import path
from books.views import listview, details

app_name = "books"
urlpatterns = [
    path('', listview, name='list'),
    path("<int:book_id>", details, name="details"),
]