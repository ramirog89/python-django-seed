from rest_framework import serializers
from src.app.models.user import User


class LoginDTO(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
