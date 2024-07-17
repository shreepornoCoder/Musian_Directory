from django.shortcuts import render, redirect
from . import forms 
from . import models
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

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

@method_decorator(login_required, name="dispatch")
class Add_Musicians(CreateView):
    model = models.Author
    form_class = forms.AuthorClass
    template_name = 'add_musicians.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Musician Added Successfully!")
        return super().form_valid(form)

class SignUpView(CreateView):
    form_class = forms.RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('homepage') 

    def form_valid(self, form):
        messages.success(self.request, "You Signed Up Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "You Singed Up UnSuccessfully!")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'SignUp'
        return context
    
class UserLoginView(LoginView):
    template_name = 'signup.html'
    success_url = reverse_lazy('homepage')

    def get_success_url(self):
        return reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, "You Logged In Successfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "Logged In Incorrectly!")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
    
def user_logout(request):
    logout(request)
    return redirect('homepage')

class UserLogOutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Logged Out Successfully!")
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return redirect('homepage')