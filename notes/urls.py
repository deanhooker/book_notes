"""Defines URL patterns for notes app."""

from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all books
    path('books/', views.books, name='books'),

    # Show chapters for a single book.
    path('books/<int:book_id>/', views.book, name='book'),

    # Show notes for a chapter.
    path('books/<int:book_id>/<int:chapter_id>/', views.chapter, name='chapter'),

    # Page for adding a new book.
    path('new_book/', views.new_book, name='new_book'),
]