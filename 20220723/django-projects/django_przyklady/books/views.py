from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def listview(request):
    books = [
        {'name': 'Pan Tadeusz', 'autor': 'Adam Mickiewicz', 'rok': '1834', 'ilosc_stron': '200'},
        {'name': 'Harry Potter', 'autor': 'JKK Rowling', 'rok': '2000', 'ilosc_stron': '350'},
        {'name': 'Hobbit', 'autor': 'JRR Tolkien', 'rok': '1937', 'ilosc_stron': '150'},
        {'name': 'Przedwiośnie', 'autor': 'Stefan Żeromski', 'rok': '1924', 'ilosc_stron': '125'}
    ]
    return render(request, 'books.html', {'books': books})


