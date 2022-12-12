from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from django.http import Http404

from . import serializers
from .models import Music


class MusicAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.MusicSerializer

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: serializer_class},
    )
    def get(self, request, format=None, *args, **kwargs):
        musics = Music.objects.all().order_by("-created_at")
        serializer = self.serializer_class(musics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=serializer_class, responses={status.HTTP_200_OK: serializer_class}
    )
    def post(self, request, formt=None, *args, **kwargs):
        music_data = request.data
        serializer = self.serializer_class(music_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class MusicDetailsAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.MusicSerializer

    def get_music_object(self, music_id: int) -> Music:
        try:
            return Music.objects.get(pk=music_id)
        except Music.DoesNotExist:
            raise Http404

    @swagger_auto_schema(responses={status.HTTP_200_OK: serializer_class})
    def get(self, request, pk, formt=None, *args, **kwargs):
        music_obj = self.get_music_object(pk)
        serializer = self.serializer_class(music_obj, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=serializer_class, responses={status.HTTP_200_OK: serializer_class}
    )
    def put(self, request, pk, format=None, *args, **kwargs):
        music_data = request.data
        music_obj = self.get_music_object(pk)
        serializer = self.serializer_class(data=music_data, instance=music_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None, *args, **kwargs):
        music_obj = self.get_music_object(pk)
        music_obj.delete()
        return Response({"result": "success"}, status=status.HTTP_204_NO_CONTENT)
