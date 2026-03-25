from django import forms
from .models import useraccount

class useraccountForm(forms.ModelForm):
    class Meta:
        model = useraccount
        fields  = ['firstname', 'lastname', 'email', 'phonenumber', 'role','password']