from factories.models import Model
from rest_framework.generics import ListAPIView

from ..serializers import ModelSerializerResponse


class ModelListApiView(ListAPIView):
    serializer_class = ModelSerializerResponse
    queryset = Model.objects.all()
