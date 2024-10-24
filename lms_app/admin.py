from django.contrib import admin

# Register your models here.
from .models import Genre, Book, BookCopy, Language, Author

admin.site.register(Genre)
# admin.site.register(BookCopy)
# admin.site.register(Book)
admin.site.register(Language)
# admin.site.register(Author)


# To Modify Data Displayed on Admin Dashboard - Adding More Columns
# New Class can be Created to Modify the Display

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isbn', 'author', 'display_genre', 'language')
    list_filter = ('author', 'language')

admin.site.register(Book, BookAdmin)

class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'imprint', 'due_back')
    list_filter = ('status', 'due_back')

admin.site.register(BookCopy, BookCopyAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display= ('__str__', 'date_of_birth')

admin.site.register(Author, AuthorAdmin)