from django.urls import path, include
from . import views

urlpatterns = [
    path('Add_album/', views.add_album, name='add_album'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete, name='delete_post'),
]
