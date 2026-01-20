from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    ('pro', 'pro'),
    ('simple', 'simple'),
)


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                       MaxValueValidator(70)],
                                      null=True, blank=True)
    phone_number = PhoneNumberField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name

class Country(models.Model):
    country_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=64)
    director_bio = models.TextField()
    director_age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                               MaxValueValidator(100)],
                                                    null=True, blank=True)
    director_image = models.ImageField(upload_to='director_image/', null=True, blank=True)

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=64)
    actor_bio = models.TextField()
    actor_age = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                            MaxValueValidator(100)],
                                           null=True, blank=True)
    actor_image = models.ImageField(upload_to='actor_image/', null=True, blank=True)

    def __str__(self):
        return self.actor_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=32, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=64)
    year = models.DateField()
    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    TYPES_CHOICES = (
         ('360p', '360p'),
         ('480p', '480p'),
         ('720p', '720p'),
         ('1080p', '1080p'),
         ('1080p Ultra', '1080p Ultra')
    )
    types = models.CharField(max_length=12, choices=TYPES_CHOICES, default='720p')
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.URLField()
    movie_image = models.ImageField(upload_to='movie_image/',null=True, blank=True)
    slogan = models.CharField(max_length=64, null=True, blank=True)
    status_movie = models.CharField(max_length=32, choices=STATUS_CHOICES)


class MovieLanguages(models.Model):
    Language = models.CharField(max_length=32)
    video = models.FileField(upload_to='movie_video/', null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Moments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_moments = models.ImageField(upload_to='moments_image/', null=True, blank=True)


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1,11)],
                                             null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    parent_movie = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    parent_movie = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class ReviewLike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like =  models.BooleanField(default=False)

class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class FavoriteMovie(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)