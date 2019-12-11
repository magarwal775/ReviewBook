from django.db import models
from base.models import Star, Genre, Director, Publication

class TvShow(models.Model):
    name =          models.CharField(max_length=400)
    releasedate =   models.DateField('first episode released')
    description =   models.TextField(blank=True)
    star =          models.ManyToManyField(Star)
    genre =         models.ManyToManyField(Genre)
    director=       models.ManyToManyField(Director)
    runningtime =   models.DurationField()
    totalepisode =  models.IntegerField(default=1)
    totalreview =   models.IntegerField(default=0)
    nor =           models.IntegerField(default=0)
    publication =   models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, blank=True)
    image =         models.ImageField(upload_to='tvshows/', max_length=255, null=True, blank=True)
    avgreview =     models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

class Episode(models.Model):
    show_name =     models.ForeignKey(TvShow, on_delete=models.CASCADE)
    episodename =   models.CharField(max_length=400)
    episodenumber = models.IntegerField()
    description =   models.TextField(blank=True)
    releasedate =   models.DateField('Edisode Release Date')
    director =      models.ManyToManyField(Director)
    runningtime =   models.DurationField()
    totalreview =   models.IntegerField(default=0)
    nor =           models.IntegerField(default=0)
    image =         models.ImageField(upload_to='episodes/', max_length=255, null=True, blank=True)
    avgreview =     models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.episodenumber) + ". " + self.episodename + ", " + self.show_name.name
