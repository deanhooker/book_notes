"""Defines URL patterns for notes app."""

from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all books
    path('books/', views.books, name='books'),
]