from django.contrib.auth.base_user import BaseUserManager
from serum import singleton

from src.app.models import User


@singleton
class UserRepository(BaseUserManager):

    def get_all(self):
        return User.objects.all()

    def get_by_id(self, id):
        return User.objects.get(id=id)

    def save(self, user_entity):
        user = User(username=user_entity['username'],
                    password=user_entity['password'],
                    email=self.normalize_email(user_entity['email']))
        user.set_password(user_entity['password'])
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

    def update(self, user_entity, id):
        user = User.objects.get(id=id)
        user.username = user_entity['username']
        user.email = user_entity['email']
        if 'password' in user_entity:
            user.set_password(user_entity['password'])
        user.save()
        return user

    def delete(self, id):
        user = User.objects.get(id=id)
        user.delete()
