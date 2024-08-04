from factories.models import Color
from rest_framework import serializers


class ColorSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            "id",
            "name",
        ]
