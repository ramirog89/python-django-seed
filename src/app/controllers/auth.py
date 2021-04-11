from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase

from drf_yasg.utils import swagger_auto_schema

from src.app.dtos.auth import LoginDTO
from src.app.dtos.token import TokenDto


class AuthenticationController(TokenViewBase, viewsets.GenericViewSet):
    permission_classes = ()

    def get_serializer_class(self):
        if self.action == 'login':
            return TokenDto
        else:
            return TokenDto

    @swagger_auto_schema(request_body=LoginDTO, responses={200: TokenDto}, security=[])
    def login(self, request, *args, **kwargs):
        print(request.data)
        token_response = super().post(request, args, kwargs)
        return token_response

    def logout(self, request):
        # print(tokenResponse.data['access'])
        print(request.META['HTTP_AUTHORIZATION'])
        # self.blackList.append(request.META)
        return Response(None)
