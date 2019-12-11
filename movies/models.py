from django.db import models
from base.models import Genre, Star, Director, Publication

class Movie(models.Model):
    name =         models.CharField(max_length=400)
    releasedate =  models.DateField('date released')
    description =  models.TextField(blank=True)
    stars =        models.ManyToManyField(Star)
    genre =        models.ManyToManyField(Genre)
    director =     models.ForeignKey(Director, on_delete=models.CASCADE)
    runningtime =  models.DurationField()
    totalreview =  models.IntegerField(default=0)
    nor =          models.IntegerField(default=0)
    publication =  models.ForeignKey(Publication,on_delete=models.CASCADE, null=True, blank=True)
    image =        models.ImageField(upload_to='movies/', max_length=255, null=True, blank=True)
    avgreview =    models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
