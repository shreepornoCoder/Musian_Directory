from django.urls import path, include
from . import views


urlpatterns = [
    path('Add_Musicians/', views.Add_Musicians.as_view(), name='add_musicians'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
]
