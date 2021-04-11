from serum import dependency

from django.contrib.auth.hashers import check_password

from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase

from src.app.repositories.user import UserRepository
from src.app.models import User
from src.app.dtos.auth import LoginDTO
from src.app.dtos.token import TokenDto, TokenDTO


class TokenObject(object):
    pass


@dependency
class AuthenticationService(TokenViewBase):
    request = None
    format_kwarg = None
    
    def get_serializer_class(self):
        return TokenDTO

    def authenticate(self, request, *args, **kwargs):
        token_response = super().post(request, args, kwargs)
        token = TokenObject()
        token.token = token_response.data['access']
        return TokenDto(token).data
