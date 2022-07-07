from django.urls import path
from . import views

urlpatterns = [
  
  path('poses/', views.PoseList.as_view()),
  path('poses/<int:pk>', views.PoseDetail.as_view()),
  path('sequences/', views.SequenceList.as_view()),
  path('sequences/<int:pk>', views.SequenceDetail.as_view()),

]