from django.urls import path
from . import views

urlpatterns = [

    # When a URL is accessed, the Function in the View.py file will be accessed and run
    path('', views.index, name='index'), # Route is Main URL = /library/
    path('about-us/', views.about_us, name='about_us'), # Route is: /library/about-us/

    path('languages/', views.LanguageListView.as_view(), name='languages'),
    path('genres/', views.GenreListView.as_view(), name='genres'),

    # Create a URL for Library Member User Group - To See all Their Borrowed Book when Logged In
    path('my-books/', views.BorrowedBooksByUserListView.as_view(), name='my-books'),

    # Create a URL for Staff - To See all the Borrowed Books when Logged In
    path('all-borrowed/',views.BorrowedBooksAllListView.as_view(), name='all-borrowed'),

    # Create a URL for Logged In Staff - To Renew Due Back Date
    path('book/<uuid:pk>/renew/',views.renew_book_librarian, name='renew-book-librarian'),

]


# Author Model Related's Paths
urlpatterns += [

    # READ Operation
    path('authors/', views.AuthorListView.as_view(), name='authors'), # URL Route is: main/authors/
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name= 'author_detail'), # URL Route is: main/authors/author.id

    # UPDATE Operation
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),

    # CREATE Operation
    path('author/create/', views.AuthorCreateView.as_view(), name='author-create'),

    # DELETE Operation
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
]

# Book Model's Related Paths
urlpatterns += [
    
    path('books/', views.BookListView.as_view(), name='books'), # URL Route is: main/books/
    
# '''
# 1. We have to create the BookListView Class in views.py

# 2. In views.py - we will have to create the Class this way
#     class BookListView(generic.ListView):
#         model = Book

# 3. The above Class - as Generic View Class is used - will search for HTML Template Automatically 
# in Folder : templates/app_name/<model_name>_list.html
# ** app_name -- newly created folder name (same name as app_name)
# *** <model_name>_list.html -- how the file should be named

# 4. So in our Project, we have to save our HTML file in a new created folder "lms_app"
# and HTML File as book_list.html (e.g. Model Name = Book)
# '''

    # This <int:pk> refers to the Primary Key: ID of each book 
    # - so it will be based off the order which the Book is added
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),   # URL Route is: main/books/book.id
    # Name will have to be the same as the get_absolute_url Name in models.py

# '''
# 1. We have to create the BookDetailView Class in views.py

# 2. In views.py - we will have to create the Class this way
#     class BookDetailView(generic.DetailView):
#         model = Book

# 3. The above Class - as Generic View Class is used - will search for HTML Template Automatically 
# in Folder : templates/app_name/<model_name>_detail.html
# ** app_name -- newly created folder name (same name as app_name)
# *** <model_name>_detail.html -- how the file should be named

# 4. So in our Project, we have to save our HTML file in a new created folder "lms_app"
# and HTML File as book_detail.html (e.g. Model Name = Book)
# '''

    # CREATE BOOK
    path('book/create/', views.BookCreateView.as_view(), name='book-create'),
    
    # UPDATE BOOK
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),

    # DELETE BOOK
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),


# BookCopy's RELATED PATHS
    # UPDATE
    path('book/<uuid:pk>/update/', views.BookCopyUpdate.as_view(), name='bookcopy-update'),
    # CREATE
    path('bookcopy/create/', views.BookCopyCreateView.as_view(), name='bookcopy-create'),
    # DELETE
    path('book/<uuid:pk>/delete/', views.BookCopyDeleteView.as_view(), name='bookcopy-delete'),

]
