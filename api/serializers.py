from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import User
from artist.models import Song


class SongSerializer(serializers.ModelSerializer):
    audio = serializers.FileField()
    class Meta:
        model = Song
        fields = ('id','artist','title', 'audio',)


class SongAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('audio',)

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }
