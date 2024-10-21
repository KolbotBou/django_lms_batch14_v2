from django.shortcuts import render

# Import all the Models we need to Access Data and Information to be Shown on Page Below
from .models import Book, BookCopy, Genre, Author, Language

# Import Generic Function for BookListView Class
from django.views import generic

# Create your views here.

# When MAIN URL /library is accessed, index.html file will be viewed / shown
def index(request):

    # To Count All The Details / Data in The Library Database for Shown
    num_books = Book.objects.all().count()
    
    num_book_copies = BookCopy.objects.all().count()

    num_genres = Genre.objects.all().count()

    num_authors = Author.objects.all().count()

    num_languages = Language.objects.all().count()

        # Counting Total Number of Book Copy with Status 'a' : 'available
    num_book_available = BookCopy.objects.filter(status__exact='a').count()

    # Creating a PAYLOAD Dictionary containing Key-Value for Database Info we want to show
    payloads = {
        'num_books' : num_books,
        'num_book_copies' : num_book_copies,
        'num_genres' : num_genres,
        'num_authors' : num_authors,
        'num_languages' : num_languages,
        'num_book_available' : num_book_available
    }

    return render(request, 'index.html', context=payloads)

###
'''Context is a Key-Value Objects that we use to HOLD VALUES we RENDER from MODELS'''
###

# When about_us URL is accessed, about_us.html file will be viewed / shown
def about_us(request):
    return render(request,'about_us.html')


# Creating a BookListView Class for showing the information on the URL - Using Generic View Class

class BookListView(generic.ListView):
    model = Book
# Django will select all available Book's Data and Store it to a Variable book_list 
# Basically: <model_name>_list

class BookDetailView(generic.DetailView):
    model = Book
# Django will select all available Book's Data and Store it to a Variable <model_name>.<dictionrary>
# Basically: <model_name>.datafield
# DetailView Class is a Dictionary Datatype

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

class LanguageListView(generic.ListView):
    model = Language

class GenreListView(generic.ListView):
    model = Genre