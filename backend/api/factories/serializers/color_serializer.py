from rest_framework import serializers

from backend.factories.models import Color


class ColorSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            "id",
            "name",
        ]
