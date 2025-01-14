from rest_framework import serializers
from . import models
from django.contrib.auth.models import User #type: ignore


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco
        fields = '__all__'

class MeuUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
       