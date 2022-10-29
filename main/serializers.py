from rest_framework import serializers
from .models import *


class LigadoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Ligado
        fields = '__all__'


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


class AreaNameSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = AreaName
        fields = '__all__'


class InternalAreaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = InternalArea
        fields = '__all__'


class StaticRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = StaticRoutine
        fields = '__all__'


class NonStaticRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = NonStaticRoutine
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Log
        fields = '__all__'


class EletricLogSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = EletricLog
        fields = '__all__'


class LigadoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Ligado
        fields = '__all__'


class AccessToCaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = AccessToCa
        fields = '__all__'


'''
class UsuariosGETSerializer(serializers.ModelSerializer):
    idAssinaturaFK = AssinaturaSerializer(read_only=True)
    class Meta:
        many = True
        model = Usuarios
        fields = '__all__'
'''
