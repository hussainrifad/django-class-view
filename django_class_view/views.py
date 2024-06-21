from django.views.generic import ListView
from artist.models import ArtistModel

class ArtistListView(ListView):
    model = ArtistModel
    template_name = 'home.html'

    def get_context_data(self, *kwargs):
        context = super().get_context_data(*kwargs)
        context['artists'] = ArtistModel.objects.all()
        context['user'] = self.request.user
        return context