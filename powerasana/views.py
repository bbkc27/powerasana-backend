from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Sequence, Pose
from .serializers import SequenceSerializer, PoseSerializer, UserSerializer, MyTokenObtainPairSerializer

# Create your views here.

class CreateUser(generics.CreateAPIView):
  model = get_user_model()
  permission_classes = [permissions.AllowAny]
  serializer_class = UserSerializer


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

  def post(self, request, *args, **kwargs):
    print(request, request.user)
    request.data['user'] = request.user.username
    return self.create(request, *args, **kwargs)

class SequenceDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = SequenceSerializer
  queryset = Sequence.objects.all()
  permission_classes = [permissions.AllowAny]

  def put(self, request, *args, **kwargs):
    print(request)
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

