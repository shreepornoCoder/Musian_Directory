from django import forms 
from . models import Author
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AuthorClass(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

        labels = {
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "email" : "Email",
            "phone_num" : "Phone Number",
            "instrument" : "Instrument Name",
        }

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':"required"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':"required"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':"required"}))

    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email']