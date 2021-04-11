from serum import inject

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenViewBase

from drf_yasg.utils import swagger_auto_schema

from src.app.dtos.auth import LoginDTO
from src.app.dtos.token import TokenDto
from src.app.services.authentication import AuthenticationService


@swagger_auto_schema(methods=['POST'], request_body=LoginDTO, responses={200: TokenDto}, security=[])
@api_view(['POST'])
@permission_classes([AllowAny])
@inject
def login(request, service: AuthenticationService):
    try:
        token = service.authenticate(payload=request.data)
        return Response(token, status=status.HTTP_200_OK)
    except Exception as error:
        print(error)
        return Response({ 'error': str(error) }, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['POST'], responses={200: None})
@api_view(['POST'])
@inject
def logout(request):
    try:
        tokenResponse = super().post(request, args, kwargs)
        return tokenResponse
    except Exception as error:
        return Response({ 'error': str(error) }, status=status.HTTP_400_BAD_REQUEST)
