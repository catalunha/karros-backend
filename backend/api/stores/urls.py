from django.urls import path

from .views import (
    VehicleAllListAPIView,
    VehicleAllRetrieveAPIView,
    VehicleUserCreateAPIView,
    VehicleUserDeleteAPIView,
    VehicleUserListAPIView,
    VehicleUserUpdateAPIView,
)

urlpatterns = [
    path(
        "vehicle/all/",
        VehicleAllListAPIView.as_view(),
    ),
    path(
        "vehicle/user/",
        VehicleUserListAPIView.as_view(),
    ),
    path(
        "vehicle/create/",
        VehicleUserCreateAPIView.as_view(),
    ),
    path(
        "vehicle/read/<str:pk>/",
        VehicleAllRetrieveAPIView.as_view(),
    ),
    path(
        "vehicle/update/<str:pk>/",
        VehicleUserUpdateAPIView.as_view(),
    ),
    path(
        "vehicle/delete/<str:pk>/",
        VehicleUserDeleteAPIView.as_view(),
    ),
]
