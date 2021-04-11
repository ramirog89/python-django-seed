from serum import inject

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema

from src.app.dtos.auth import LoginDTO
from src.app.dtos.token import TokenDto
from src.app.services.authentication import AuthenticationService


@swagger_auto_schema(methods=['POST'], request_body=LoginDTO, responses={200: TokenDto}, security=[])
@api_view(['POST'])
@permission_classes([AllowAny])
@inject
def login(request, service: AuthenticationService):
    dto = LoginDTO(data=request.data)
    if  dto.is_valid():
        token = service.authenticate(request)
        return Response(token, status=status.HTTP_200_OK)
    else:
        return Response(dto.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['POST'], responses={200: None})
@api_view(['POST'])
@inject
def logout(request):
    ''' here should be implemented a token black list mechanism or something '''
    return Response(None, status=status.HTTP_200_OK)
