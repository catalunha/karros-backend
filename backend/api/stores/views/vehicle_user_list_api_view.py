from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from backend.stores.models.vehicle import Vehicle

from ..serializes.vehicle_serializer_response import VehicleSerializerResponse


class VehicleUserListAPIView(ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = VehicleSerializerResponse
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "model__brand__id",
        "model__id",
        "color__id",
        "value",
        "year",
    ]

    def get_queryset(self):
        return Vehicle.objects.filter(
            is_sold=False,
            user=self.request.user,
        )
