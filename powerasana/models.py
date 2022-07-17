from pyexpat import model
from django.db.models.deletion import CASCADE
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
import uuid



# Create your models here.


class Pose(models.Model):
  sanskrit = models.CharField(max_length=100, default='')
  english_name = models.CharField(max_length=100, default='')
  cues = ArrayField(
        models.CharField(max_length=250, blank=True), size=3,
        )
  image_url = models.TextField(default='')


  def __str__(self):
    return self.english_name


class Sequence(models.Model):
  uuid = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4)
  intention = models.CharField(max_length=200, default='')
  duration = models.DurationField()
  intensity = models.CharField(max_length=100, default='')
  peak_pose = models.CharField(max_length=100, default='')
  poses = models.ManyToManyField(Pose, related_name="sequence_list", blank=True)
  author = models.ForeignKey(User, related_name='sequences', on_delete=models.CASCADE, default=1)
  
  def __str__(self):
    return self.intention



