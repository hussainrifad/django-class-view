from django.urls import path
from . import views

urlpatterns = [
  path('add_album/', views.AddAlbumCreateView.as_view(), name='addalbum')
]