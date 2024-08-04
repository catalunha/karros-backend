from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers import MeSerializer


class MeRetrieveAPIView(RetrieveAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user
