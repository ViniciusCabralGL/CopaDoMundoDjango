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

'''
class UsuariosGETSerializer(serializers.ModelSerializer):
    idAssinaturaFK = AssinaturaSerializer(read_only=True)
    class Meta:
        many = True
        model = Usuarios
        fields = '__all__'
'''
