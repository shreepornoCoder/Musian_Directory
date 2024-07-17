from django.shortcuts import render, redirect
from . import forms 
from . import models
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView

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

class AddAlbumView(CreateView):
    model = models.Album
    form_class = forms.Album 
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')

def edit_post(request, id):
    post = models.Album.objects.get(pk=id)
    post_form = forms.Album(instance=post)

    if request.method == 'POST':
        post_form = forms.Album(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    
    return render(request, 'add_album.html', {'forms':post_form})

class EditView(UpdateView):
    model = models.Album
    form_class = forms.Album
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'


def delete(request, id):
    post = models.Album.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

class DeleteView(DeleteView):
    model = models.Album
    template_name = "delete.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')