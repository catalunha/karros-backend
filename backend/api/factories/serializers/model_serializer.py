from rest_framework import serializers

from backend.factories.models import Model

from .brand_serializer import BrandSerializerResponse


class ModelSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = [
            "id",
            "name",
        ]


class ModelSerializerResponse2(serializers.ModelSerializer):
    brand = BrandSerializerResponse()

    class Meta:
        model = Model
        fields = [
            "id",
            "name",
            "brand",
        ]
