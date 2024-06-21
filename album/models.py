from django.db import models
from artist.models import ArtistModel
from django.utils import timezone

# Create your models here.

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=50)
    artist = models.ForeignKey(ArtistModel, related_name='albums', on_delete=models.CASCADE)
    release_date = models.DateField(default=timezone.now)
    rating = models.CharField(max_length=5, default=0, choices=[('zero','0'),('one','1'),('two','2'),('three','3'),('four','4'),('five','5')])