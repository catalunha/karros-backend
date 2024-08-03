from core.models import BaseModel
from django.db import models

from .brand import Brand


class Model(BaseModel):
    name = models.CharField(max_length=256)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="models",
    )
