from rest_framework import serializers

from backend.stores.models.vehicle import Vehicle


class VehicleSerializerRequest(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "model",
            "color",
            "image",
            "value",
            "year",
            "description",
            "owner",
        ]
