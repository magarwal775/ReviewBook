from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name

class Director(models.Model):
    director_name =        models.CharField(max_length=200)
    director_dob =         models.DateField('Date of Birth')
    director_description = models.TextField(blank=True)

    def __str__(self):
        return self.director_name

class Star(models.Model):
    star_name =          models.CharField(max_length=200)
    star_dob =           models.DateField('Date of Birth')
    star_description =   models.TextField(blank=True)

    def __str__(self):
        return self.star_name

class Publication(models.Model):
    publication_name =         models.CharField(max_length=500)
    publication_description =  models.TextField(blank=True)

    def __str__(self):
        return self.publication_name
