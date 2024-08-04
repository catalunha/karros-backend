from factories.models import Color
from rest_framework.generics import ListAPIView

from ..serializers import ColorSerializerResponse


class ColorListApiView(ListAPIView):
    serializer_class = ColorSerializerResponse
    queryset = Color.objects.all()
