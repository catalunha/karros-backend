from factories.models import Brand
from rest_framework.generics import ListAPIView

from ..serializers import BrandSerializerResponse


class BrandListApiView(ListAPIView):
    serializer_class = BrandSerializerResponse
    queryset = Brand.objects.all()
