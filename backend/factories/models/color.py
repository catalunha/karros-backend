from django.db import models

from backend.core.models import BaseModel


class Color(BaseModel):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"{self.name}"
