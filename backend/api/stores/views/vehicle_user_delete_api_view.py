from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from backend.stores.models.vehicle import Vehicle

from ..serializes.vehicle_serializer_request import VehicleSerializerRequest


class VehicleUserDeleteAPIView(DestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = VehicleSerializerRequest

    def get_queryset(self):
        return Vehicle.objects.filter(user=self.request.user)
