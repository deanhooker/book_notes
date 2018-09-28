from django.shortcuts import render

from .models import Book

# Create your views here.
def index(request):
    """Return the home page for Notes."""
    return render(request, 'notes/index.html')

def books(request):
    """Return all books."""
    books = Book.objects.order_by('date_added')
    context = {'books': books}
    return render(request, 'notes/books.html', context)

def book(request, book_id):
    """Return notes related to a single book."""
    book = Book.objects.get(id=book_id)
    chapters = book.chapter_set.order_by('id')
    context = {'book': book, 'chapters': chapters}
    return render(request, 'notes/book.html', context)
    