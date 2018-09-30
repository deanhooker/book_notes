from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Book, Chapter
from .forms import BookForm

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
    """Return chapters related to a single book."""
    book = Book.objects.get(id=book_id)
    chapters = book.chapter_set.order_by('id')
    context = {'book': book, 'chapters': chapters}
    return render(request, 'notes/book.html', context)

def chapter(request, book_id, chapter_id):
    """Return notes related to a chapter."""
    book = Book.objects.get(id=book_id)
    chapter = Chapter.objects.get(id=chapter_id)
    notes = chapter.note_set.order_by('id')
    context = {'book': book, 'chapter': chapter, 'notes': notes}
    return render(request, 'notes/note.html', context)

def new_book(request):
    """Add a new book."""
    if request.method != 'POST':
        # No data submitted; create blank form.
        form = BookForm()
    else:
        # POST data submitted; process data.
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notes:books'))

    context = {'form': form}
    return render(request, 'notes/new_book.html', context)