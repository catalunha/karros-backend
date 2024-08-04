from factories.models import Model
from rest_framework import serializers


class ModelSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = [
            "id",
            "name",
        ]
