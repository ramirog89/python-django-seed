from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenDto(serializers.Serializer):
    token = serializers.CharField()


# class TokenDTO(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['email'] = user.email
#         return token
