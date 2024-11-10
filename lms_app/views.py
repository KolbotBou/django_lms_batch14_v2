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

# Import LoginRequiredMixin for Restriction - Generic Class Based View
# So Only Logged In Users can View the Class (that used this LoginRequiredMixin)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create a View for Library Member User Group - To See all Their Borrowed Book when Logged In
class BorrowedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookCopy

    # Instead of using Default HTML File Name Convention (model_list.html) - we do as below to have Custom HTML Template File Name
    template_name = 'lms_app/borrowed_books_by_user.html'

    # Create this Function - so only Logged In Users' Related Objects are shown
    def get_queryset(self):
        return (
            BookCopy.objects.filter(borrower = self.request.user).order_by('due_back')
        )
    

# Import PermissionRequiredMixin for Logged In Staff Only View
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create a View for Staff - To see All Borrowed Books from the Library
class BorrowedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    model = BookCopy
    
    permission_required = 'lms_app.can_mark_returned'

    template_name = 'lms_app/bookcopy_list_borrowed_all.html'

    # Create this Function - so ONLY LOGGED IN STAFF can view this data
    def get_queryset(self):
        return (BookCopy.objects.filter(status__exact='o').order_by('due_back')
                )