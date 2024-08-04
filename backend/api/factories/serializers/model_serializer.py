from rest_framework import serializers

from backend.factories.models import Model


class ModelSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = [
            "id",
            "name",
        ]
