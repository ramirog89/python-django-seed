from serum import dependency

from rest_framework_simplejwt.views import TokenViewBase

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
