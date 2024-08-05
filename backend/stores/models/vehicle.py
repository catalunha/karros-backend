from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from backend.core.models import BaseModel
from backend.factories.models import Color, Model
from backend.users.models import User


def image_upload_to(instance, filename):
    return f"vehicle/image/{instance.pk}/{filename}"


class Vehicle(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="vehicles",
    )
    model = models.ForeignKey(
        Model,
        on_delete=models.SET_NULL,
        related_name="vehicles",
        null=True,
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.SET_NULL,
        related_name="vehicles",
        null=True,
    )
    image = models.ImageField(
        upload_to=image_upload_to,
        null=True,
        blank=True,
    )
    value = models.DecimalField(
        max_digits=11,
        decimal_places=2,
    )
    year = models.PositiveSmallIntegerField(
        default=date.today().year,
        validators=[
            MinValueValidator(1850),
            MaxValueValidator(date.today().year),
        ],
    )
    description = models.CharField(max_length=256)
    owner = models.CharField(max_length=256)
    is_sold = models.BooleanField(default=False)
