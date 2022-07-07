from rest_framework import serializers
from .models import Pose, Sequence



class PoseSerializer(serializers.HyperlinkedModelSerializer):
  sequences = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = Pose
    fields = ('id', 'sanskrit', 'english_name', 'cues', 'image_url', 'sequences')


class SequenceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Sequence
    fields = ('uuid', 'user_string', 'intention', 'intensity', 'duration', 'peak_pose')