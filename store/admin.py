from django.contrib import admin
from .models import (UserProfile, Category, Country,  Director,
                     Actor, Genre, Movie, MovieLanguages, Moments,
                     Rating, Review, ReviewLike, Favorite, FavoriteMovie, History )
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

class GenreInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Genre
    extra = 1

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    inlines = [GenreInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class MovieLanguagesInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1

class MomentsInline(admin.TabularInline):
    model = Moments
    extra = 1

@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    inlines = [MovieLanguagesInline, MomentsInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile),
admin.site.register(Country),
admin.site.register(Director),
admin.site.register(Actor),
admin.site.register(Rating),
admin.site.register(Review),
admin.site.register(ReviewLike),
admin.site.register(Favorite),
admin.site.register(FavoriteMovie),
admin.site.register(History),
