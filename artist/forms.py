from .models import ArtistModel
from django import forms


class ArtistForm(forms.ModelForm):
    class Meta:
        model = ArtistModel
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'id':'required'}),
            'last_name': forms.TextInput(attrs={'id':'required'}),
            'email': forms.EmailInput(attrs={'id':'required'})
        }

        labels = {
            'email' : 'Email Address'
        }

        help_texts = {
            'phone_number' : 'Enter phone number with country code'
        }