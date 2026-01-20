from .models import (UserProfile, Country, Director, Actor,
                     Genre, Movie, MovieLanguages, Moments,
                     Rating, Favorite, FavoriteMovie, History)

from .serializers import (UserProfileSerializer, CountrySerializer, CountryDetailSerializer,
                          DirectorSerializer, DirectorDetailSerializer,
                          ActorSerializer, ActorDetailSerializer, GenreSerializer,
                          GenreDetailSerializer, MovieListSerializer, MovieDetailSerializer,
                          MovieLanguagesSerializer, MomentsSerializer, RatingSerializer,
                          FavoriteSerializer, FavoriteMovieSerializer, HistorySerializer,
                          )

from rest_framework import viewsets, generics


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CountryAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer


class DirectorAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer


class ActorAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetailView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer


class GenreAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer


class MovieLanguagesViewSet(viewsets.ModelViewSet):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializer


class MomentsViewSet(viewsets.ModelViewSet):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer