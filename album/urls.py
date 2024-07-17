from django.urls import path, include
from . import views

urlpatterns = [
    path('Add_album/', views.AddAlbumView.as_view(), name='add_album'),
    path('edit/<int:id>', views.EditView.as_view(), name='edit_post'),
    path('delete/<int:id>', views.DeleteView.as_view(), name='delete_post'),
]
