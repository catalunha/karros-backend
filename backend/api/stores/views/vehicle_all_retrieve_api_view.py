from rest_framework.generics import RetrieveAPIView

from backend.stores.models.vehicle import Vehicle

from ..serializes.vehicle_serializer_response import VehicleSerializerResponse


class VehicleAllRetrieveAPIView(RetrieveAPIView):
    serializer_class = VehicleSerializerResponse
    queryset = Vehicle.objects.all()
