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

# class LogIn(TokenObtainPairView):
#   permission_classes = [permissions.AllowAny]
#   serializer_class = MyTokenObtainPairSerializer

class PoseList(generics.ListCreateAPIView):
  serializer_class = PoseSerializer
  queryset = Pose.objects.all()
  permission_classes = [permissions.IsAuthenticated]

class PoseDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PoseSerializer
  queryset = Pose.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SequenceList(generics.ListCreateAPIView):
  serializer_class = SequenceSerializer
  queryset = Sequence.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def post(self, request, *args, **kwargs):
    print(request.user.username)
    request.data['user'] = request.user.username
    return super().post(request, *args, **kwargs)

class SequenceDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = SequenceSerializer
  queryset = Sequence.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
