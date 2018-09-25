from django.contrib import admin

# Register your models here.
from notes.models import Book, Chapter, Note

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Note)