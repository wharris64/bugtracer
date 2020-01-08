from django.forms import ModelForm
from django import forms
from bugtrace.models import Ticket
from django.contrib.auth.models import User
from bugtrace import views

class Add_Ticket(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

class LoginUser(forms.Form):
    username = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(min_length =  4)

class Edit(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

class UserAdd(forms.Form):
    username = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(min_length =  4)
    


