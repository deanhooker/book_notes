from django.shortcuts import render

from .models import Book, Chapter

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