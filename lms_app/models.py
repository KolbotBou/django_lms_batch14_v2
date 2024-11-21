from django.db import models

# Need to import these Functions so we can use in the following Coding
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

from django.urls import reverse     # To Generate URLs by reversing URL Pattern

# Create your models here.

# These MODElS will be shown and accessible on Django Admin Dashboard

# Create 'Genre' Model / Table for 'Book'
class Genre(models.Model):

    # Attributes / Data of 'Genre'
    name = models.CharField('Genre', 
                            max_length=150, 
                            unique=True,
                            help_text='Please Enter a Book Genre (e.g. Science, Fantasy, Finance...)')
    
    # Functions of 'Genre'
    def __str__(self):
        return self.name        # This is the String Representation of 'Genre' Model
    
    def get_absolute_url(self):
        # Return the URL to access particular Genre Data based on ID - Showing all Details
        return reverse("genre_detail", args=[str(self.id)])
    
    # A Sub Meta-Class of 'Genre' Model
    class Meta:
        ordering = ['name']     # The 'Genre' List is arranged based on 'Name'

        # Use Constraint to Prevent Duplicated Genre.Name Field (e.g. Science, Science, science)
        constraints = [UniqueConstraint(Lower('name'),
                name = 'genre_name_case_insensitive_unique',
                violation_error_message = 'Genre Already Exists'
                )
        ]

# Create 'Language' Model
class Language(models.Model):

    # Attributes of Language
    language = models.CharField(max_length=100,
                                unique=True,
                                help_text='Please Enter a Language')

    # Functions of Language
    def __str__(self):
        return self.language
    
    def get_absolute_url(self):
        return reverse("language_detail", args=[str(self.id)])
    
        # Meta Sub-Class
    class Meta:
        ordering = ['language']

        # Use Constraint to Prevent Duplicated Language
        constraints = [UniqueConstraint(Lower('language'),
                                        name = 'language_name_case_insensitive_unique', 
                                        violation_error_message = 'Language Already Exists.')]

# Create 'Author' Model
class Author(models.Model):

    # Attributes
    first_name = models.CharField(max_length=200, help_text='Please Enter Author\'s First Name')
    last_name = models.CharField(max_length=200, help_text='Please Enter Author\'s Last Name')

    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    # Functions
    def __str__(self):      
        # This Function will be how Data appears for ForeignKey - Selection Choices and how it appear on Admin Dashboard
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.id)])
    
        # Meta Sub-Class
    class Meta:
        ordering = ['first_name']

        # Adding Permission for Author Update and Creation
        permissions = [("update_author", "Update Author"), ("create_author", "Create Author")
                    ]

    # Creating this Function to use in HTML - so Full Name can be Display in Author List, and can be Click to Access Author Detail
    def display_name(self):
        return f'{self.first_name} {self.last_name}'

# Create 'Book' Model
class Book(models.Model):
    
    # Attributes of Book
    title = models.CharField('Title',
                             max_length=300,
                             help_text='Please Enter Book Title')
    
    summary = models.TextField('Description',
                               max_length=1500,
                               help_text='Please Enter Book Description')
    
    isbn = models.CharField('ISBN-13',max_length=13, unique=True, 
                            help_text='13 Characters <a href="https://isbnsearch.org/">ISBN Search </a>')
    

    # Creating the Connections between Book and Genre - Language - Author
    genre = models.ManyToManyField(Genre, help_text='Select one or many Genre for the Book')

    language = models.ForeignKey(Language, 
                                 on_delete=models.RESTRICT,
                                 help_text='Select a Language for the Book',
                                 null=True)

    author = models.ForeignKey(Author,
                               on_delete=models.RESTRICT,
                               help_text='Select a Author for the Book',
                               null=True)

    # Functions of Book
    def __str__(self):
        return f'{self.id}. {self.title}'

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])

    def display_genre(self):    # This is to Show Book Genres on Admin Dashboard
        genres = self.genre.all()
        # Retrieving all genres associated with Book Instance
        
        # Creating List of Genre Names
        genre_name_list = [genre.name for genre in genres]

        return ', '.join(genre_name_list)
        # Joining the List into a Single String Separated by Comma

    # To Have the Header appeared as 'Genre'
    display_genre.short_description = 'Genre'

    # Subclass - Meta for Book
    class Meta:
        ordering = ['id']

# Create 'Book Instances' Model
import uuid     # To create unique ID for each Book Copy
from datetime import date   # To Generate Auto Date & Time
from django.conf import settings        # Required to Assign User as 'Borrower'

class BookCopy(models.Model):

    # BookCopy Attributes
    uniqueid = models.UUIDField('UUID', 
                                primary_key=True,
                                default=uuid.uuid4,
                                help_text='Unique ID for this Book Copy in Library')
    
    imprint = models.CharField(max_length=200)

    due_back = models.DateField(null=True, blank=True)

    # Creating This 'Borrower' Datafield - so Logged In User could borrow a Book Copy
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 null=True)
    
    loan_status= (
        ('m','Maintenance'),
        ('o','On Loan'),
        ('a','Available'),
        ('r','Reserved')
    )

    status = models.CharField(max_length=1, 
                              choices=loan_status, 
                              blank=True,
                              default='m',
                              help_text='Book Availability' )

    # Creating the Connections between BookCopy and Book
    book = models.ForeignKey(Book,
                             on_delete=models.RESTRICT,
                             null=True)

    # BookCopy Functions
    def __str__(self):
        return f'{self.uniqueid} [{self.book.title}]'
    
    def get_absolute_url(self):
        return reverse("bookcopy_detail", args=[str(self.id)])
    
    @property       # Custom Function (outside of Django) - which can be called to USE
    def is_over_due(self):
        return bool(date.today() > self.due_back)
    # To check if the Due Back Date has been Passed / OVERDUED

        # Meta Sub_Class
    class Meta:
        ordering = ['due_back', 'imprint']

            # Adding this Permissions Code - To Have Custom Permission for Staff/Admin Account
        permissions = [("can_mark_returned", "Set book as Returned"),
                    ]