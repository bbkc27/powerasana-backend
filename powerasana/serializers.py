from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from traitlets import default
from .models import Pose, Sequence

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

  def create(self, validated_data):

    user = UserModel.objects.create(
      username=validated_data['username'],
      password=validated_data['password']
    )

    return user


  class Meta:
    model = UserModel
    fields = ('id', 'username', "password")

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token

class PoseSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Pose
    fields = ('english_name', 'id', 'sanskrit', 'cues', 'image_url')


class SequenceSerializer(serializers.HyperlinkedModelSerializer):

  poses = serializers.SlugRelatedField(many=True, read_only=True, slug_field='english_name')
  author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

  class Meta:
    model = Sequence
    fields = ('id', 'author', 'uuid', 'intention', 'intensity', 'duration', 'peak_pose', 'poses')