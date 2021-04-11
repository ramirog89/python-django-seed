from rest_framework import serializers


class LoginDTO(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=128)
