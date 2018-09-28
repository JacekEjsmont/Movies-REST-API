from django.db import models


class Movie(models.Model):
    Title = models.CharField(max_length=50)
    Year = models.CharField(max_length=10, blank=True)
    Rated = models.CharField(max_length=10, blank=True)
    Released = models.CharField(max_length=20, blank=True)
    Runtime = models.CharField(max_length=20, blank=True)
    Genre = models.CharField(max_length=100, blank=True)
    Director = models.CharField(max_length=100, blank=True)
    Writer = models.CharField(max_length=200, blank=True)
    Actors = models.CharField(max_length=500, blank=True)
    Plot = models.CharField(max_length=500, blank=True)
    Language = models.CharField(max_length=50, blank=True)
    Country = models.CharField(max_length=50, blank=True)
    Awards = models.CharField(max_length=100, blank=True)
    Poster = models.CharField(max_length=1000, blank=True)
    Metascore = models.CharField(max_length=50, blank=True)
    imdbRating = models.CharField(max_length=50, blank=True)
    imdbVotes = models.CharField(max_length=50, blank=True)
    imdbID = models.CharField(max_length=50, blank=True)
    Type = models.CharField(max_length=100, blank=True)
    DVD = models.CharField(max_length=50, blank=True)
    BoxOffice = models.CharField(max_length=100, blank=True)
    Production = models.CharField(max_length=100, blank=True)
    Website = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Title


class Comment(models.Model):
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    Text = models.CharField(max_length=1000)
