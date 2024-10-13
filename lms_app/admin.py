from django.contrib import admin

# Register your models here.
from .models import Genre, Book, BookCopy

admin.site.register(Genre)
# admin.site.register(BookCopy)
# admin.site.register(Book)


# To Modify Data Displayed on Admin Dashboard - Adding More Columns
# New Class can be Created to Modify the Display

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isbn', 'display_genre')

admin.site.register(Book, BookAdmin)

class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'imprint', 'due_back')
    list_filter = ('status', 'due_back')

admin.site.register(BookCopy, BookCopyAdmin)