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

""" Language MODEL VIEW """
class LanguageListView(generic.ListView):
    model = Language

""" GENRE MODEL VIEW """
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
        return (
            BookCopy.objects.filter(status__exact='o').order_by('due_back')
            )

    # Function View - to Show Form for Due Back Date Renewal
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Import Created Form Class from forms.py
from lms_app.forms import RenewBookForm

from django.urls import reverse

import datetime

@login_required
@permission_required('lms_app.can_mark_returned', raise_exception=True)

def renew_book_librarian(request, pk):

    # Function to View Specific Book by Librarian
    book_copy = get_object_or_404(BookCopy, pk=pk)

    # If The Form is SUBMITTED - The Form Data is Processed
    if request.method == 'POST':

        # Create a Form Object for Populating with user-submitted data from the POST request.
        form = RenewBookForm(request.POST)

        # Check if the Form is Valid
        if form.is_valid():

            # Process Data in form.clean_renewal_date -- and saving the UPDATED data to MODEL.due_back Field
            book_copy.due_back = form.cleaned_data['renewal_date']    # book_copy is the INHERIT of BookCopy Model
            book_copy.save()

            # Redirect to another URL
            return HttpResponseRedirect(reverse('all-borrowed'))
        
    # Create a Default Value Form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(days=21)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    renewal_bookcopy_payloads = {
        'form': form,
        'book_copy': book_copy,
    }
    return render(request, 'lms_app/book_renew_libratian.html', context=renewal_bookcopy_payloads)

""" AUTHOR MODEL VIEW """
class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

# AuthorUpdate Class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    # Not Recommended to Add more Fields - Potential Security Risks
    fields = '__all__'
    permission_required = 'lms_app.update_author'    

class AuthorCreateView(PermissionRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    permission_required = 'lms_app.create_author'

class AuthorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Author
    permission_required = 'lms_app.delete_author'

    success_url = reverse_lazy('authors')   
    # This is used to redirect to after successfully handling a form submission
    # reverse_lazy is a function in Django module that reverse (resolve) a URL pattern name into an actual URL.

    # To Validate Author Delete Operation always go success_url which is Author List by Default
    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse('author-delete', kwargs={'pk': self.object.pk})
            )


""" BOOK MODEL VIEW """
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

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    permission_required = 'lms_app.add_book'

class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    permission_required = 'lms_app.change_book'

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    permission_required = 'lms_app.delete_book'

    success_url = reverse_lazy('books')

""" BookCopy MODEL VIEW """
class BookCopyUpdate(PermissionRequiredMixin, UpdateView):
    model = BookCopy
    fields = ['imprint', 'due_back', 'borrower', 'status', 'book']
    permission_required = 'lms_app.change_bookcopy'

    success_url = reverse_lazy('books')

class BookCopyCreateView(PermissionRequiredMixin, CreateView):
    model = BookCopy
    fields = '__all__'
    permission_required = 'lms_app.add_bookcopy'

    success_url = reverse_lazy('books')

class BookCopyDeleteView(PermissionRequiredMixin, DeleteView):
    model = BookCopy
    permission_required = 'lms_app.delete_bookcopy'

    success_url = reverse_lazy('books')