from serum import inject, dependency

from django.contrib.auth.hashers import check_password

from rest_framework_simplejwt.tokens import RefreshToken

from src.app.repositories.user import UserRepository
from src.app.models import User
from src.app.dtos.auth import LoginDTO
from src.app.dtos.token import TokenDto

@dependency
class AuthenticationService:

    @inject
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def authenticate(self, payload, **kwargs):
        try:
            login = LoginDTO(data=payload)
            login.is_valid(raise_exception=True)
            user_valid = self.repo.get_by_username(payload['username'])
        except User.DoesNotExist:
            raise Exception('User Does Not Exist.')

        pwd_valid = check_password(payload['password'], user_valid.password)

        if user_valid and pwd_valid:
            token = RefreshToken.for_user(user_valid)
            return { 'token': str(token) }
        raise Exception('Invalid password.')
