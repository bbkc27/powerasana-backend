from rest_framework import serializers
from .models import Pose, Sequence

class SequenceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Sequence
    fields = ('id', 'uuid', 'user_string', 'intention', 'intensity', 'duration', 'peak_pose', 'poses')

class PoseSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Pose
    fields = ('id', 'sanskrit', 'english_name', 'cues', 'image_url')