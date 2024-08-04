from django.db import models

from backend.core.models import BaseModel

from .brand import Brand


class Model(BaseModel):
    name = models.CharField(max_length=256)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="models",
    )

    def __str__(self) -> str:
        return f"{self.name}-{self.brand}"
