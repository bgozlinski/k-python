from django.shortcuts import render

from books.services import BookService, book_service


# Create your views here.

def listview(request):
    books = book_service.get_all_books()
    return render(
        request=request,
        template_name="books.html",
        context={'books': books}
    )


def details(request, book_id: int):
    book = book_service.get_book(book_id)
    return render(
        request=request,
        template_name="books_details.html",
        context={'book': book}
    )


