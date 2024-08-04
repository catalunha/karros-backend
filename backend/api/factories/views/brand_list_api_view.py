from rest_framework.generics import ListAPIView

from backend.factories.models import Brand

from ..serializers import BrandSerializerResponse


class BrandListApiView(ListAPIView):
    serializer_class = BrandSerializerResponse
    queryset = Brand.objects.all()
