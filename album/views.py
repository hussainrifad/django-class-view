from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib import messages
from .models import AlbumModel
from .forms import AlbumForm

# Create your views here.

class AddAlbumCreateView(CreateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, *kwargs)
        else:
            return redirect('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Album Added Successfully')
        return super().form_valid(form=form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid Input')
        return super().form_invalid(form=form)
