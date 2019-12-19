from django.db import models
from base.models import Genre, Publication

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

def upload_location(instance, filename):
    file_path = 'games/{game_name}/{filename}'.format(
        game_name=str(instance.name), filename=filename
    )
    return file_path

class Game(models.Model):
    name =          models.CharField(max_length=400)
    releasedate =   models.DateField('date released')
    description =   models.TextField(blank=True)
    genre =         models.ManyToManyField(Genre)
    size =          models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    totalreview =   models.IntegerField(default=0)
    totalrating =   models.IntegerField(default=0)
    publication =   models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, blank=True)
    image =         models.ImageField(upload_to=upload_location, null=False, blank=False)
    avgrating =     models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

class GameReview(models.Model):
    title =              models.CharField(max_length=50, null=False, blank=False)
    body =               models.TextField(max_length=5000, null=False, blank=False)
    rating =             models.IntegerField(default=1)
    date_published =     models.DateTimeField(auto_now_add=True, verbose_name="Date Reviewed")
    date_updated =       models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    author =             models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game =               models.ForeignKey(Game, on_delete=models.CASCADE)
    slug =               models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(GameReview, self).save(*args, **kwargs)
        game = Game.objects.get(id=self.game_id)
        r = self.rating
        game.totalreview = game.totalreview + 1
        game.totalrating = game.totalrating + r
        game.save()
        game.avgrating = game.totalrating/game.totalreview
        game.save()

    def delete(self, *args, **kwargs):
        game = Game.objects.get(id=self.game_id)
        r = self.rating
        game.totalreview = game.totalreview - 1
        game.totalrating = game.totalrating - r
        game.save()
        if(game.totalreview != 0):
            game.avgrating = game.totalrating/game.totalreview
        else:
            game.avgrating = 0
        game.save()
        super(GameReview, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(GameReview, self).save(*args, **kwargs)
        game = Game.objects.get(id=self.game_id)
        allreview = GameReview.objects.filter(game=game)
        totalrat = 0
        for each in allreview:
            totalrat = totalrat + each.rating
        game.totalrating = totalrat
        game.totalreview = len(allreview)
        game.save()
        game.avgrating = game.totalrating/game.totalreview
        game.save()

@receiver(post_delete, sender=Game)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_review_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.game.name + "-" + instance.author.username + "-" +instance.title)

pre_save.connect(pre_save_review_receiver, sender=GameReview)
