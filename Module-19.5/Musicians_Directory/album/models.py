from django.db import models
from musicians.models import Musician
import datetime
# Create your models here.
class Album(models.Model):
    RATINGS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    album_name = models.CharField(max_length=200)
    owner=models.ForeignKey(Musician,on_delete=models.CASCADE)
    album_relese_date = models.DateField(null=True, blank=True)
    ratings = models.IntegerField(choices=RATINGS_CHOICES,default=1)
    def __str__(self) -> str:
        return self.album_name
