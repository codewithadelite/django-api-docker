from django.contrib import admin

from .models import Artist, Genre, Music

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Music)
