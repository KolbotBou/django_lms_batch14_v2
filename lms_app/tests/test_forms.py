import datetime
from django.test import TestCase
from django.utils import timezone

from lms_app.forms import RenewBookForm

class RenewBookFormTest(TestCase):

    # TCFORM001: Verify if the date field label is correctly set in the form
    def test_renew_form_date_field_label(self):
        form = RenewBookForm()
        self.assertTrue(form.fields['renewal_date'].label is None 
                        or form.fields['renewal_date'].label == 'renewal date')
        
    # TCFORM002: Verify if the Help Text is correctly included in the form
    def test_renew_form_date_field_help_text(self):
        form = RenewBookForm()
        self.assertEqual(form.fields['renewal_date'].help_text, 'Enter a Date between Now and 4 Weeks (Default 3 Weeks).')

    # TCFORM003: Test if an Error is raised when a date in the past has been entered
    def test_renew_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        # Minus 1 day - to check if the date in the form is equal to Yesterday
        form = RenewBookForm({'renewal_date': date})
        self.assertFalse(form.is_valid())

    # TCFORM004: Test if an Error is raised when a date above 4 weeks has been entered
    def test_renew_form_date_over_4weeks(self):
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form = RenewBookForm({'renewal_date': date})
        self.assertFalse(form.is_valid())

    # TCFOR005: Verify that the correct renewal date has been entered
    def test_renew_form_date_next_one_day(self):
        date = datetime.date.today() + datetime.timedelta(days=2)
        form = RenewBookForm({'renewal_date': date})
        self.assertTrue(form.is_valid())
