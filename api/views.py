from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import parsers
from accounts.models import User
from artist.models import Song
from django.contrib.auth import authenticate
from .serializers import UserSerializer, SongSerializer, SongAudioSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


class FileUploadView(APIView):
    parser_class = (parsers.FileUploadParser,)


    def get(self,request):
        artists = Song.objects.all()
        serializer = SongSerializer(artists,many=True)
        return Response(serializer.data)

    def put(self, request, filename, format=None):
        file_serializer = SongSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        file_serializer = SongSerializer(data=request.data)
        print(request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (AllowAny,)

    def pre_save(self, obj):
        obj.audio = self.request.FILES.get('audio')

    def create(self, request, *args, **kwargs):
        print(request.data)
        artist = request.data['artist']
        title = request.data['title']
        audio = request.FILES.get('audio')  # request.data['audio']

        song = Song.objects.create(
            artist=artist,
            title=title,
            audio=audio
        )
        song.save()
        response = {'success': True, 'id': song.id, 'artist': song.artist, 'audio': song.audio}
        return Response(response, status.HTTP_201_CREATED)

        # if song.save():
        #     response = {'success': True ,'id': song.id, 'artist':song.artist,'audio': song.audio}
        #     return Response(response,status.HTTP_201_CREATED)
        # else:
        #     response = {'success': False,'error': 'OOps song creation failed!'}
        #     return Response(response,status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['POST'])
    def login(self, request, pk=None):
        print(request.data)
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            response = {'success': True, 'message': 'Correct account details', 'user_id': user.id, 'email': email}
            return Response(response, status.HTTP_200_OK)
        else:
            response = {'success': False, 'message': 'Invalid user credentials', 'email': email}
            return Response(response, status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.create_user(email=email, password=password)
        user.save()
        if user is not None:
            Token.objects.create(user=user)
            response = {'success': True,
                        'email': email,
                        'user_id': user.id
                        }
            return Response(response, status.HTTP_201_CREATED)
        else:
            response = {'success': False, 'error': 'User creation failed'}
            return Response(response, status.HTTP_400_BAD_REQUEST)
