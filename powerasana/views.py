from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, permissions

from .models import Sequence, Pose
from .serializers import SequenceSerializer, PoseSerializer

# Create your views here.

class PoseList(generics.ListCreateAPIView):
  serializer_class = PoseSerializer
  queryset = Pose.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PoseDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PoseSerializer
  queryset = Pose.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SequenceList(generics.ListCreateAPIView):
  serializer_class = SequenceSerializer
  queryset = Sequence.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  # def post(self, request, *args, **kwargs):
  #   print(request.user.username)
  #   request.data['user_string'] = request.user.username
  #   return super().post(request, *args, **kwargs)

class SequenceDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = SequenceSerializer
  queryset = Sequence.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
