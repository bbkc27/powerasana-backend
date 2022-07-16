from django.urls import path
from . import views

urlpatterns = [
  
  path('signup/', views.CreateUser.as_view()),
  # path('login/', views.LogIn.as_view()),

  path('poses/', views.PoseList.as_view()),
  path('poses/<int:pk>', views.PoseDetail.as_view(), name='pose_detail'),
  path('sequences/', views.SequenceList.as_view()),
  path('sequences/<int:pk>', views.SequenceDetail.as_view()),

]