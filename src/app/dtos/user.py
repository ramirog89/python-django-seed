from rest_framework import serializers
from src.app.models.user import User

class UserDto(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'is_staff']


class UserCreateDto(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_active', 'is_staff']


class UserUpdateDto(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
        optional_fields = ['password', 'is_active', 'is_staff']
