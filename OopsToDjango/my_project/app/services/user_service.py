from .base_service import BaseService

class CreateUserService(BaseService):
    def __init__(self, username):
        self.username = username

    def validate(self):
        if not self.username:
            raise ValueError("Username required")

    def execute(self):
        return {
            "username": self.username,
            "status": "created"
        }
