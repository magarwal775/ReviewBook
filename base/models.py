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
    genre_name=models.CharField(max_length=200)
    def __str__(self):
        return self.genre_name

class Director(models.Model):
    director_name = models.CharField(max_length=200)
    director_dob = models.DateField('Date of Birth')
    director_description = models.TextField()
    def __str__(self):
        return self.director_name

class Star(models.Model):
    Star_name = models.CharField(max_length=200)
    Star_dob = models.DateField('Date of Birth')
    Star_description = models.TextField()
    def __str__(self):
        return self.Star_name

class Publication(models.Model):
    Publication_name = models.CharField(max_length= 500)
    Publication_description = models.TextField()
    def __str__(self):
        return self.Publication_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=400)
    movie_date = models.DateField('date released')
    movie_description = models.TextField()
    movie_star = models.ManyToManyField(Star)
    movie_genre= models.ForeignKey(Genre,on_delete=models.CASCADE)
    movie_director= models.ForeignKey(Director,on_delete=models.CASCADE)
    movie_runningtime = models.IntegerField()
    movie_totalreview = models.IntegerField()
    movie_nor = models.IntegerField()
    movie_publication = models.ForeignKey(Publication,on_delete=models.CASCADE, null= True , blank = True)
    movie_image = models.ImageField(upload_to='movies/' , max_length = 255 , null = True , blank = True)
    def __str__(self):
        return self.movie_name

class Game(models.Model):
    game_name = models.CharField(max_length=400)
    game_date = models.DateField('date released')
    game_description = models.TextField()
    game_genre= models.ForeignKey(Genre,on_delete=models.CASCADE)
    game_size= models.DecimalField(max_digits=6, decimal_places=2)
    game_totalreview = models.IntegerField()
    game_nor = models.IntegerField()
    game_publication = models.ForeignKey(Publication,on_delete=models.CASCADE,null= True , blank = True)
    game_image = models.ImageField(upload_to= 'games/', max_length = 255 , null= True , blank = True)
    def __str__(self):
        return self.game_name
