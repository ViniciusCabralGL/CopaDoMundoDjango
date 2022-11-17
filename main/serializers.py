from rest_framework import serializers
from .models import *


class LoginLevelSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = LoginLevel
        fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = UserLogin
        fields = '__all__'


class UserLoginGetSerializer(serializers.ModelSerializer):
    level = LoginLevelSerializer(read_only=True)

    class Meta:
        many = True
        model = UserLogin
        fields = '__all__'


class SelecaoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Selecao
        fields = '__all__'


class TipoInfracaoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = TipoInfracao
        fields = '__all__'


class InfracaoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Infracao
        fields = '__all__'


class TipoJogoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = TipoJogo
        fields = '__all__'


class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Jogo
        fields = '__all__'

