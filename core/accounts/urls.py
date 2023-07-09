from django.urls import path, include
from .views import testMockServer
app_name = "accounts"

urlpatterns = [
    path("api/v1/", include("accounts.api.v1.urls")),
    path("", include("django.contrib.auth.urls")),
    path('test/',testMockServer),
]
