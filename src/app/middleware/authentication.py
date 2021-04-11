from django.contrib.auth.hashers import check_password

from src.app.models import User


class AuthenticationService:

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user_valid = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            raise User.DoesNotExist

        pwd_valid = check_password(password, user_valid.password)
        if user_valid and pwd_valid:
            return user_valid
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
