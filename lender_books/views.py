from django.shortcuts import render, get_object_or_404
from .models import Book


def books_list_view(request):
    """the request is the user attempting hit list route while logged in
        the responses render the books_list.html which populates the base
    """
    books = Book.objects.filter(user__username=request.user.username)
    context = {
        'books': books
    }

    return render(request, 'books/books_list.html', context=context)


def books_detail_view(request, pk=None):
    """the request is the user attempting hit detail route while logged in
    the responses render the books_detail.html which populates the base
    if book is not found it returns a 404 otherwise returns individual book detail
    """
    book = get_object_or_404(Book, id=pk, user__username=request.user.username)
    context = {
        'book': book,
    }
    return render(request, 'books/books_detail.html', context)