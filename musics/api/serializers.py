from rest_framework import serializers
from .models import Music


class MusicSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()

    class Meta:
        model = Music
        fields = "__all__"

    def get_artist(self, obj: Music) -> str:
        return obj.artist.name

    def get_genre(self, obj: Music) -> str:
        return obj.genre.name
