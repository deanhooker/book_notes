from django.db import models

# Create your models here.
class Book(models.Model):
    """A book the user is reading."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the title."""
        return self.title

class Chapter(models.Model):
    """A chapter in the book."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the chapter title."""
        return self.chapter_title

class Note(models.Model):
    """A note about a chapter."""
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the note."""
        return self.text