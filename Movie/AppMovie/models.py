from django.db import models
from AppUser.models import User

# Create your models here.

class Movie(models.Model):
    user = models.ManyToManyField(User)
    name_movie = models.CharField(max_length=45)
    genero_movie = models.CharField(max_length=45)
    year_movie = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name_movie']

    def __str__(self):
        return self.name_movie
