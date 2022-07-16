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


class SequenceSerializer(serializers.ModelSerializer):

  poses = serializers.PrimaryKeyRelatedField(many=True, queryset=Pose.objects.all())
  author = UserSerializer(many=False, read_only=True)

  class Meta:
    model = Sequence
    fields = ('id', 'author', 'uuid', 'intention', 'intensity', 'duration', 'peak_pose', 'poses')

class PoseSerializer(serializers.ModelSerializer):

  # sequences = serializers.PrimaryKeyRelatedField(queryset=Sequence.objects.all(), many=True)
  sequence_list = SequenceSerializer(many=True, read_only=True)

  class Meta:
    model = Pose
    fields = ('english_name', 'id', 'sanskrit', 'cues', 'image_url', 'sequence_list')


