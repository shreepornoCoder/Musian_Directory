from django.shortcuts import render, redirect
from . import forms 

# Create your views here.
def add_musicians(request):
    if request.method == "POST":
        author_form = forms.AuthorClass(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('homepage')
    else:
        author_form = forms.AuthorClass()
    return render(request, 'add_musicians.html', {"forms":author_form})