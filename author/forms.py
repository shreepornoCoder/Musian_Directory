from django import forms 
from . models import Author

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

        