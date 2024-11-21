import datetime
from django.urls import reverse
from django.utils import timezone

from django.test import TestCase

# Import User Model from Settings - Django Admin
from django.contrib.auth import get_user_model
User = get_user_model()

from lms_app.models import BookCopy, Book, Genre, Language, Author

class LoanedBookCopiesByUserListViewTest(TestCase):
    def setUp(self):
        # Create 2 Test Users
        test_user_1 = User.objects.create_user(username='testuser1', password='testuser@1234')
        test_user_2 = User.objects.create_user(username='testuser2', password='testuser@1234')
        
        test_user_1.save()
        test_user_2.save()

        # Create a Book
        test_author = Author.objects.create(first_name='John', last_name='Doe')
        test_genre = Genre.objects.create(name='Test Genre')
        test_language = Language.objects.create(language='Test Language')
        test_book = Book.objects.create(
            title = 'Book Title',
            summary = 'Book Summary',
            isbn = '1234567890123',
            language = test_language,
            author = test_author,
        )

        # Create Genre as a Separate Steps for Book - as it is ManyToMany Field to Book
        genre_objects_for_book = Genre.objects.all()
        test_book.genre.set(genre_objects_for_book)

        test_book.save()

        # Create 30 BookInstance Objects
        number_of_book_copies = 30
        for bookcopied in range(number_of_book_copies):
            return_date = timezone.localtime() + datetime.timedelta(days=bookcopied%5)
            the_borrower = test_user_1 if bookcopied % 2 else test_user_2
            status = 'm'

            BookCopy.objects.create(
                book= test_book,
                imprint = 'Test Imprtint',
                due_back = return_date,
                borrower = the_borrower,
                status = status
            )

    # TCVIEW001: Verify that User is redirected to Log In page when accessing My Borrowed Book List View
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('my-books'))
        self.assertRedirects(response,'/accounts/login/?next=/library/my-books/') 
                                        # Need to Get this Redirected URL from Server
