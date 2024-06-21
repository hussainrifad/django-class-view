from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from . import forms
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('editprofile')
        else:
            return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'User Logged in')    
        return super().form_valid(form=form)
    
    def form_invalid(self, form):
        return super().form_invalid(form=form)


class UpdateUserView(UpdateView):
    form_class = forms.UpdateProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('editprofile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'User Edited Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(request, 'Input Data is not valid')
        return self.render_to_response(self.get_context_data(form=form))

class RegisterView(CreateView):
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('userlogin')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('editprofile')
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Invalid Input Data')
        return self.render_to_response(self.get_context_data(form=form))

def userLogout(request):
    logout(request=request)
    return redirect('userlogin')