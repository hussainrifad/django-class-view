from django import forms
from .models import AlbumModel

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'

        widgets = {
            'album_name' : forms.TextInput(attrs={'id':'required'}),
            'release_date' : forms.DateInput(attrs={'type':'date'}),
        }
        