from django.shortcuts import render, redirect
from . import forms 
from . import models

# Create your views here.
def add_album(request):
    if request.method == "POST":
        album_form = forms.Album(request.POST)
        if album_form:
            album_form.save()
            return redirect('homepage')
    else:
        album_form = forms.Album()
    return render(request, 'add_album.html', {"forms":album_form})

def edit_post(request, id):
    post = models.Album.objects.get(pk=id)
    post_form = forms.Album(instance=post)

    if request.method == 'POST':
        post_form = forms.Album(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    
    return render(request, 'add_album.html', {'forms':post_form})


def delete(request, id):
    post = models.Album.objects.get(pk=id)
    post.delete()
    return redirect('homepage')