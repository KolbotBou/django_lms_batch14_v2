from django.urls import path
from . import views

urlpatterns = [

    # When a URL is accessed, the Function in the View.py file will be accessed and run
    path('', views.index, name='index'), # Route is Main URL = /library/
    path('about-us/', views.about_us, name='about_us'), # Route is: /library/about-us/

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

    path('authors/', views.AuthorListView.as_view(), name='authors'), # URL Route is: main/authors/
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name= 'author_detail'), # URL Route is: main/authors/author.id

    path('languages/', views.LanguageListView.as_view(), name='languages'),
    path('genres/', views.GenreListView.as_view(), name='genres'),

    # Create a URL for Library Member User Group - To See all Their Borrowed Book when Logged In
    path('my-books/', views.BorrowedBooksByUserListView.as_view(), name='my-books'),

    # Create a URL for Staff - To See all the Borrowed Books when Logged In
    path('all-borrowed/',views.BorrowedBooksAllListView.as_view(), name='all-borrowed'),

]