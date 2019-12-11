from django.db import models
from base.models import Genre, Publication

class Game(models.Model):
    name =          models.CharField(max_length=400)
    releasedate =   models.DateField('date released')
    description =   models.TextField(blank=True)
    genre =         models.ManyToManyField(Genre)
    size =          models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    totalreview =   models.IntegerField(default=0)
    nor =           models.IntegerField(default=0)
    publication =   models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, blank=True)
    image =         models.ImageField(upload_to='games/', max_length=255, null=True, blank=True)
    avgreview =     models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
