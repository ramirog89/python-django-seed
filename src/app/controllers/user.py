from serum import inject

from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from src.app.services.user import UserService
from src.app.dtos.pagination import PaginationDto, PaginationQueryParamsDto
from src.app.dtos.user import UserDto, UserCreateDto, UserUpdateDto
from src.app.config.swagger import CustomPaginatorClass


@swagger_auto_schema(method='GET', query_serializer=PaginationQueryParamsDto, responses={200: UserDto(many=True)})
@api_view(['GET'])
@inject
def list(request, service: UserService):
    try:
        return Response(data=service.get_all(request), status=status.HTTP_200_OK)
    except Exception as error:
        return Response({ 'error': str(error) }, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='GET', responses={200: UserDto})
@api_view(['GET'])
@inject
def get(request, id, service: UserService):
    try:
        user = service.get_by_id(id)
        return Response(user, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({ 'error': str(error) }, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='POST', request_body=UserCreateDto, responses={200: UserDto})
@api_view(['POST'])
@inject
def create(request, service: UserService):
    serializer = UserCreateDto(data=request.data)
    if serializer.is_valid():
        user = service.create(request.data)
        return Response(user, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='PUT', request_body=UserUpdateDto, responses={200: UserDto})
@api_view(['PUT'])
@inject
def update(request, id, service: UserService):
    serializer = UserUpdateDto(data=request.data)
    if serializer.is_valid():
        user = service.update(request.data, id)
        return Response(user, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='DELETE', responses={200: None})
@api_view(['DELETE'])
@inject
def delete(request, id, service: UserService):
    try:
        service.delete(id)
        return Response(status=status.HTTP_200_OK)
    except Exception as error:
        return Response({ 'error': str(error) }, status=status.HTTP_400_BAD_REQUEST)
