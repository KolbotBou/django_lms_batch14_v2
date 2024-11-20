import datetime

from django import forms

from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text='Enter a Date between Now and 4 Weeks (Default 3 Weeks).')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a Date is not in the PAST
        if data < datetime.date.today():
            raise ValidationError( 'Invalid Date - Renewal Date in the Past' )
        
        # Check if a Date is in the Allowed Range (4 Weeks from Today)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Invalid Date - Renewal Date is Over 4 Weeks')
        
        # Remember to always Return Cleaned Data
        return data