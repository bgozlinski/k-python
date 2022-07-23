from django.urls import path
from posts.views import postview

app_name = "posts"
urlpatterns = [
    path('', postview, name='list'),
]