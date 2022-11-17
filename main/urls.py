from django.urls import path
from .views import *

urlpatterns = [
    path("loginLevel/", LoginLevelAPIView.as_view(), name='loginLevel'),
    path('loginLevel/<int:pk>/', LoginLevelAPIView.as_view(), name='loginLevelParameters'),

    path("userLogin/", UserLoginAPIView.as_view(), name='userLogin'),
    path('userLogin/<int:pk>/', UserLoginAPIView.as_view(), name='userLoginParameters'),

    path("selecao/", SelecaoAPIView.as_view(), name='selecao'),
    path('selecao/<int:pk>/', SelecaoAPIView.as_view(), name='selecaoParameters'),

    path("tipoInfracao/", TipoInfracaoAPIView.as_view(), name='tipoInfracaoAPIView'),
    path('tipoInfracao/<int:pk>/', TipoInfracaoAPIView.as_view(), name='tipoInfracaoAPIViewParameters'),

    path("infracao/", InfracaoAPIView.as_view(), name='infracao'),
    path('infracao/<int:pk>/', InfracaoAPIView.as_view(), name='infracaoParameters'),

    path("tipoJogo/", TipoJogoAPIView.as_view(), name='tipoJogoAPIView'),
    path('tipoJogo/<int:pk>/', TipoJogoAPIView.as_view(), name='tipoJogoAPIViewParameters'),

    path("jogo/", JogoAPIView.as_view(), name='Jogo'),
    path('jogo/<int:pk>/', JogoAPIView.as_view(), name='JogoParameters'),
]

