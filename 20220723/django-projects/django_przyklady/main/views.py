from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html',
                  {
                      'a_list': [1,2,3],
                      'autor': {'name': 'Adam','last_name': 'Mickiewicz'}
                  })


def greetings(request):
    return HttpResponse('Hello')
