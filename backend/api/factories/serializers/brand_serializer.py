from rest_framework import serializers

from backend.factories.models import Brand


class BrandSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "id",
            "name",
        ]
