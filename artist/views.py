from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView
from .forms import ArtistForm, ArtistModel
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class AddArtistCreateView(CreateView):
    form_class = ArtistForm
    model = ArtistModel
    success_url = reverse_lazy('home')
    template_name = 'add_artist.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('userlogin')  
     
    def form_valid(self, form):
        messages.success(self.request, 'Artist Added Successfully')
        return super().form_valid(form=form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid Input')
        return super().form_valid(form=form)

class DeleteArtistDeletView(DeleteView):
    model = ArtistModel
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')
