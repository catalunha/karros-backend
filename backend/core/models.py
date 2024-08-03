from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    # TODO: maybe use uuid7 smaller and fester to insert, need to look into
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
