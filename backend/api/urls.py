from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path(
        "auth/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
urlpatterns += [
    path(
        "me/",
        include("backend.api.me.urls"),
    ),
]
urlpatterns += [
    path(
        "factories/",
        include("backend.api.factories.urls"),
    ),
]
urlpatterns += [
    path(
        "stores/",
        include("backend.api.stores.urls"),
    ),
]
