from django.db import models
from core.models import BaseModel
from .user import User


class JWTToken(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.TextField()
    expires_at = models.DateTimeField()
    is_blacklisted = models.BooleanField(default=False)
