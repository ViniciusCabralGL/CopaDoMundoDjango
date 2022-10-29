from django.urls import path
from .views import *

urlpatterns = [
    path("loginLevel/", LoginLevelAPIView.as_view(), name='loginLevel'),
    path('loginLevel/<int:pk>/', LoginLevelAPIView.as_view(), name='loginLevelParameters'),

    path("userLogin/", UserLoginAPIView.as_view(), name='userLogin'),
    path('userLogin/<int:pk>/', UserLoginAPIView.as_view(), name='userLoginParameters'),

]

