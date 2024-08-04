from rest_framework.generics import ListAPIView

from backend.factories.models import Model

from ..serializers import ModelSerializerResponse


class ModelListApiView(ListAPIView):
    serializer_class = ModelSerializerResponse
    queryset = Model.objects.all()
