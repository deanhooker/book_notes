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