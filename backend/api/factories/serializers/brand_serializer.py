from factories.models import Brand
from rest_framework import serializers


class BrandSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "id",
            "name",
        ]
