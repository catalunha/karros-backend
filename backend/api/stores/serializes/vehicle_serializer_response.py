from rest_framework import serializers

from backend.api.factories.serializers.color_serializer import ColorSerializerResponse
from backend.api.factories.serializers.model_serializer import ModelSerializerResponse2
from backend.api.me.serializers.me_serializer import MeSerializer
from backend.stores.models.vehicle import Vehicle


class VehicleSerializerResponse(serializers.ModelSerializer):
    user = MeSerializer()
    model = ModelSerializerResponse2()
    color = ColorSerializerResponse()

    class Meta:
        model = Vehicle
        fields = [
            "id",
            "user",
            "model",
            "color",
            "image",
            "value",
            "year",
            "description",
            "owner",
        ]
