from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    name                = models.CharField(max_length=150)

    description         = models.CharField(max_length=3000, null=True)
    released_date       = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movies-list")


class ShowTime(models.Model):
    movie               = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name="show_times")

    timing              = models.DateTimeField()
    location            = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse("showtime-list", kwargs={"movie_id": self.movie_id})
