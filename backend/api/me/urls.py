from django.urls import path

from .views import MeRetrieveAPIView

urlpatterns = [
    path("", MeRetrieveAPIView.as_view()),
]
