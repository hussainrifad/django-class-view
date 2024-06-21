from django.urls import path
from . import views

urlpatterns = [
    path('add_artist/', views.AddArtistCreateView.as_view(), name='addartist'),
    
]