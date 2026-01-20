from rest_framework import serializers
from .models import (UserProfile, Country, Director, Actor,
                     Genre, Movie, MovieLanguages, Moments,
                     Rating, Review, ReviewLike, Favorite, FavoriteMovie, History)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_image', 'movie_name', 'year',
                  'country', 'genre', 'status_movie']


class CountryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['country_name']


class DirectorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ['director_name', 'director_bio', 'director_age',
                  'director_image']


class ActorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['actor_name', 'actor_bio', 'actor_age',
                  'actor_image']


class GenreDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['genre_name']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video', 'movie']


class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Rating
        fields = ['id', 'user', 'movie', 'parent_movie', 'stars', 'comment', 'created_date']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'user', 'movie', 'comment', 'parent_movie', 'created_date']


class ReviewLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewLike
        fields = ['id', 'user', 'review', 'like']


class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%d-%m_Y')
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)


    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country',
                  'director', 'actor', 'genre', 'types',
                  'movie_time', 'description', 'movie_trailer',
                  'movie_image', 'status_movie']




class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'