from django.urls import path
from posts.views import postview


urlpatterns = [
    path('', postview),
]