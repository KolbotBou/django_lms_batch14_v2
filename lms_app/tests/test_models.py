from django.test import TestCase
from lms_app.models import Author

# Write Unit Test for Model Class: Author

class AuthorTestCase(TestCase):
    
    @classmethod
    
    def setUpTestData(cls):
        Author.objects.create(first_name='John', last_name='Doe')

    # TestCase: TC001 - Test First Name Label
    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label,'first name')

    # TestCase: TC003 - Test if first_name Field can hold 200 Characters Max
    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 200)

    # TestCase: TC06 - Test get_absolute_url Method - Return URL Path '/library/author/<int:pk>/'
    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/library/author/1')