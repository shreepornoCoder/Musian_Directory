from django import forms 
from . models import Album

class Album(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

        # labels = {
        #     "first_name" : "First Name",
        #     "last_name" : "Last Name",
        #     "email" : "Email",
        #     "phone_num" : "Phone Number",
        #     "instrument" : "Instrument Name",
        # }
        widgets={
            "release_date":forms.DateInput(attrs={'type':'date'}),
        }

        