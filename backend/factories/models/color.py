from core.models import BaseModel
from django.db import models


class Color(BaseModel):
    name = models.CharField(max_length=256)
