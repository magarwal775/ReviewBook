from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, dob,  password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an unique username")
        if not first_name:
            raise ValueError("Users must enter First Name")
        if not last_name:
            raise ValueError("Users must enter Last Name")
        if not dob:
            raise ValueError("Users must enter Date of Birth")

        user = self.model(
                email=self.normalize_email(email),
                username=username,
                first_name=first_name,
                last_name=last_name,
                dob=dob,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, dob,  password):
        user = self.create_user(
                email=self.normalize_email(email),
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                dob=dob,
        )

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email =        models.EmailField(verbose_name="EmailId", max_length=100, unique=True)
    username =     models.CharField(max_length=40, unique=True)
    date_joined =  models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login =   models.DateTimeField(verbose_name="Last Login", auto_now=True)
    is_admin =     models.BooleanField(default=False)
    is_active =    models.BooleanField(default=True)
    is_staff =     models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name =   models.CharField(max_length=100)
    last_name =    models.CharField(max_length=100)
    dob =          models.DateField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','dob']

    objects = MyAccountManager()

    def __str__(self):
        return self.email + ", " + self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True

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

class Movie(models.Model):
    movie_name =         models.CharField(max_length=400)
    movie_date =         models.DateField('date released')
    movie_description =  models.TextField(blank=True)
    movie_star =         models.ManyToManyField(Star)
    movie_genre =        models.ManyToManyField(Genre)
    movie_director =     models.ForeignKey(Director, on_delete=models.CASCADE)
    movie_runningtime =  models.DurationField()
    movie_totalreview =  models.IntegerField(default=0)
    movie_nor =          models.IntegerField(default=0)
    movie_publication =  models.ForeignKey(Publication,on_delete=models.CASCADE, null=True, blank=True)
    movie_image =        models.ImageField(upload_to='movies/', max_length=255, null=True, blank=True)
    movie_avgreview =    models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.movie_name

class Game(models.Model):
    game_name =          models.CharField(max_length=400)
    game_date =          models.DateField('date released')
    game_description =   models.TextField(blank=True)
    game_genre =         models.ManyToManyField(Genre)
    game_size =          models.DecimalField(max_digits=6, decimal_places=2)
    game_totalreview =   models.IntegerField(default=0)
    game_nor =           models.IntegerField(default=0)
    game_publication =   models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, blank=True)
    game_image =         models.ImageField(upload_to='games/', max_length=255, null=True, blank=True)
    game_avgreview =     models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.game_name

class TvShow(models.Model):
    show_name =          models.CharField(max_length=400)
    show_date =          models.DateField('first episode released')
    show_description =   models.TextField(blank=True)
    show_star =          models.ManyToManyField(Star)
    show_genre =         models.ManyToManyField(Genre)
    show_director=       models.ManyToManyField(Director)
    show_runningtime =   models.DurationField()
    show_totalepisode =  models.IntegerField(default=1)
    show_totalreview =   models.IntegerField(default=0)
    show_nor =           models.IntegerField(default=0)
    show_publication =   models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, blank=True)
    show_image =         models.ImageField(upload_to='tvshows/', max_length=255, null=True, blank=True)
    show_avgreview =     models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.show_name

class Episode(models.Model):
    episode_show_name =   models.ForeignKey(TvShow, on_delete=models.CASCADE)
    episode_name =        models.CharField(max_length=400)
    episode_number =      models.IntegerField()
    episode_description = models.TextField(blank=True)
    episode_date =        models.DateField('Edisode Release Date')
    episode_director =    models.ManyToManyField(Director)
    episode_runningtime = models.DurationField()
    episode_totalreview = models.IntegerField(default=0)
    episode_nor =         models.IntegerField(default=0)
    episode_image =       models.ImageField(upload_to='episodes/', max_length=255, null=True, blank=True)
    episode_avgreview =   models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.episode_number) + ". " + self.episode_name + ", " + self.episode_show_name.show_name
