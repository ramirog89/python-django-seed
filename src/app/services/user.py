from serum import inject, dependency

from src.app.repositories.user import UserRepository
from src.app.dtos import UserDto
from src.app.utils.pagination import paginate


@dependency
class UserService:

    @inject
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_by_id(self, id):
        try:
            return self.repo.get_by_id(id)
        except:
            return None

    def get_all(self, request):
        return paginate(self.repo.get_all(), request, UserDto)

    def create(self, user):
        created_user = self.repo.save(user)
        return UserDto(created_user).data

    def update(self, user, id):
        updated_user = self.repo.update(user, id)
        return UserDto(updated_user).data

    def delete(self, id):
        try:
            self.repo.delete(id)
        except Exception as error:
            raise Exception(error)
