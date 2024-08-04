from rest_framework.generics import ListAPIView

from backend.factories.models import Color

from ..serializers import ColorSerializerResponse


class ColorListApiView(ListAPIView):
    serializer_class = ColorSerializerResponse
    queryset = Color.objects.all()
