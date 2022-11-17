import requests
from .models import *
from .serializers import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
import threading
import time


class LoginLevelAPIView(APIView):
    def get(self, request, pk=''):
        if pk == '':
            dados = LoginLevel.objects.all()
            serializer = LoginLevelSerializer(dados, many=True)
            return Response(serializer.data)
        else:
            dados = LoginLevel.objects.get(id=pk)
            serializer = LoginLevelSerializer(dados)
            return Response(serializer.data)

    def put(self, request, pk=''):
        dados = LoginLevel.objects.get(id=pk)
        serializer = LoginLevelSerializer(dados, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dados = LoginLevel.objects.get(id=pk)
        dados.delete()
        return Response({"msg": "Apagado com sucesso"})

    def post(self, request):
        serializer = LoginLevelSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserLoginAPIView(APIView):
    def get(self, request, pk=''):
        if 'user' in request.GET:
            userID = request.GET['user']
            user = UserLogin.objects.filter(idUserFK=userID)
            serializer = UserLoginGetSerializer(user, many=True)
            return Response(serializer.data)
        elif pk == '':
            dados = UserLogin.objects.all()
            serializer = UserLoginSerializer(dados, many=True)
            return Response(serializer.data)
        else:
            dados = UserLogin.objects.get(id=pk)
            serializer = UserLoginSerializer(dados)
            return Response(serializer.data)

    def put(self, request, pk=''):
        dados = UserLogin.objects.get(id=pk)
        serializer = UserLoginSerializer(dados, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dados = UserLogin.objects.get(id=pk)
        dados.delete()
        return Response({"msg": "Apagado com sucesso"})

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SelecaoAPIView(APIView):
    def get(self, request, pk=''):
        if pk == '':
            dados = Selecao.objects.all()
            serializer = SelecaoSerializer(dados, many=True)
            return Response(serializer.data)

        dados = Selecao.objects.get(id=pk)
        serializer = SelecaoSerializer(dados)
        return Response(serializer.data)

    def put(self, request, pk=''):
        dados = Selecao.objects.get(id=pk)
        serializer = SelecaoSerializer(dados, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dados = Selecao.objects.get(id=pk)
        dados.delete()
        return Response({"msg": "Apagado com sucesso"})

    def post(self, request):
        serializer = SelecaoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TipoInfracaoAPIView(APIView):
    def get(self, request, pk=''):
        if pk == '':
            dados = TipoInfracao.objects.all()
            serializer = TipoInfracaoSerializer(dados, many=True)
            return Response(serializer.data)

        dados = TipoInfracao.objects.get(id=pk)
        serializer = TipoInfracaoSerializer(dados)
        return Response(serializer.data)

    def put(self, request, pk=''):
        dados = TipoInfracao.objects.get(id=pk)
        serializer = TipoInfracaoSerializer(dados, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dados = TipoInfracao.objects.get(id=pk)
        dados.delete()
        return Response({"msg": "Apagado com sucesso"})

    def post(self, request):
        serializer = TipoInfracaoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class InfracaoAPIView(APIView):
    def get(self, request, pk=''):
        if 'selecao' in request.GET:
            selecao = request.GET['selecao']
            selecao = Infracao.objects.filter(selecao=selecao)
            serializer = SelecaoSerializer(selecao, many=True)
            return Response(serializer.data)

        if pk == '':
            dados = Infracao.objects.all()
            serializer = InfracaoSerializer(dados, many=True)
            return Response(serializer.data)

        dados = Infracao.objects.get(id=pk)
        serializer = InfracaoSerializer(dados)
        return Response(serializer.data)

    def put(self, request, pk=''):
        dados = Infracao.objects.get(id=pk)
        serializer = InfracaoSerializer(dados, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dados = Infracao.objects.get(id=pk)
        dados.delete()
        return Response({"msg": "Apagado com sucesso"})

    def post(self, request):
        serializer = InfracaoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TipoJogoAPIView(APIView):
    def get(self, request, pk=''):
        if 'tipoJogo' in request.GET:
            tipoJogo = request.GET['tipoJogo']
            tipoJogo = TipoInfracao.objects.filter(tipoJogo=tipoJogo)
            serializer = TipoJogoSerializer(tipoJogo, many=True)
            return Response(serializer.data)

        if pk == '':
            dados = TipoJogo.objects.all()
            serializer = TipoJogoSerializer(dados, many=True)
            return Response(serializer.data)

        dados = TipoJogo.objects.get(id=pk)
        serializer = TipoJogoSerializer(dados)
        return Response(serializer.data)

    def put(self, request, pk=''):
        dados = TipoJogo.objects.get(id=pk)
        serializer = TipoJogoSerializer(dados, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dados = TipoJogo.objects.get(id=pk)
        dados.delete()
        return Response({"msg": "Apagado com sucesso"})

    def post(self, request):
        serializer = TipoJogoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class JogoAPIView(APIView):
    def get(self, request, pk=''):
        if pk == '':
            dados = Jogo.objects.all()
            serializer = JogoSerializer(dados, many=True)
            return Response(serializer.data)
        else:
            dados = Jogo.objects.get(id=pk)
            serializer = JogoSerializer(dados)
            return Response(serializer.data)

    def put(self, request, pk=''):
        dados = Jogo.objects.get(id=pk)
        serializer = JogoSerializer(dados, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dados = Jogo.objects.get(id=pk)
        dados.delete()
        return Response({"msg": "Apagado com sucesso"})

    def post(self, request):
        serializer = JogoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
