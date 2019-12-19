from django.db import models
from base.models import Star, Genre, Director, Publication

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

def upload_location_series(instance, filename):
    file_path = 'series/{series_name}/{filename}'.format(
        series_name=str(instance.name), filename=filename
    )
    return file_path

def upload_location_episode(instance, filename):
    file_path = 'series/{series_name}/{season_number}/{episode_number}/{filename}'.format(
        series_name=str(instance.show_name.name), season_number=str(instance.season_number), episode_number=str(instance.episode_number), filename=filename
    )
    return file_path


class Series(models.Model):
    name =           models.CharField(max_length=400)
    release_date =   models.DateField('First Episode Released')
    description =    models.TextField(blank=True)
    star =           models.ManyToManyField(Star)
    genre =          models.ManyToManyField(Genre)
    director=        models.ManyToManyField(Director)
    running_time =   models.DurationField()
    total_episode =  models.IntegerField(default=1)
    total_season =   models.IntegerField(default=1)
    total_review =   models.IntegerField(default=0)
    nor =            models.IntegerField(default=0)
    publication =    models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, blank=True)
    image =          models.ImageField(upload_to=upload_location_series, null=False, blank=False)
    avg_review =     models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

class Episode(models.Model):
    show_name =      models.ForeignKey(Series, on_delete=models.CASCADE)
    episode_name =   models.CharField(max_length=400)
    episode_number = models.IntegerField()
    season_number =  models.IntegerField(default=1, null=False, blank=False)
    description =    models.TextField(blank=True)
    release_date =   models.DateField('Edisode Release Date')
    director =       models.ManyToManyField(Director)
    running_time =   models.DurationField()
    totalreview =    models.IntegerField(default=0)
    totalrating =    models.IntegerField(default=0)
    image =          models.ImageField(upload_to=upload_location_episode, null=False, blank=False)
    avgrating =      models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.show_name.name + ", Season " + str(self.season_number) + ", Episode " + str(self.episode_number)

@receiver(post_delete, sender=Series)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(post_delete, sender=Episode)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

class EpisodeReview(models.Model):
    title =              models.CharField(max_length=50, null=False, blank=False)
    body =               models.TextField(max_length=5000, null=False, blank=False)
    rating =             models.IntegerField(default=1)
    date_published =     models.DateTimeField(auto_now_add=True, verbose_name="Date Reviewed")
    date_updated =       models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    author =             models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    episode =            models.ForeignKey(Episode, on_delete=models.CASCADE)
    slug =               models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(EpisodeReview, self).save(*args, **kwargs)
        episode = Episode.objects.get(id=self.episode_id)
        r = self.rating
        episode.totalreview = episode.totalreview + 1
        episode.totalrating = episode.totalrating + r
        episode.save()
        episode.avgrating = episode.totalrating/episode.totalreview
        episode.save()

    def delete(self, *args, **kwargs):
        episode = Episode.objects.get(id=self.game_id)
        r= self.rating
        episode.totalreview = episode.totalreview - 1
        episode.totalrating = episode.totalrating - r
        episode.save()
        if(episode.totalreview != 0):
            episode.avgrating = episode.totalrating/episode.totalreview
        else:
            episode.avgrating = 0
        episode.save()
        super(EpisodeReview, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(EpisodeReview, self).save(*args, **kwargs)
        episode = Episode.objects.get(id=self.episode_id)
        allreview = EpisodeReview.objects.filter(episode=episode)
        totalrat = 0
        for each in allreview:
            totalrat = totalrat + each.rating
        episode.totalrating = totalrat
        episode.totalreview = len(allreview)
        episode.save()
        episode.avgrating = episode.totalrating/episode.totalreview
        episode.save()

def pre_save_review_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.episode.show_name.name + "-" + instance.episode.episode_name + "-" + instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_review_receiver, sender=EpisodeReview)
