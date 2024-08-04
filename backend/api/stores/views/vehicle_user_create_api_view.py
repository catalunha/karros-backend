from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializes.vehicle_serializer_request import VehicleSerializerRequest


class VehicleUserCreateAPIView(CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = VehicleSerializerRequest

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
