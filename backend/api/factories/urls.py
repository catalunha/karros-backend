from django.urls import path

from .views import BrandListApiView, ColorListApiView, ModelListApiView

urlpatterns = [
    path(
        "brands/",
        BrandListApiView.as_view(),
    ),
    path(
        "colors/",
        ColorListApiView.as_view(),
    ),
    path(
        "models/",
        ModelListApiView.as_view(),
    ),
]
