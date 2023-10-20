from django.urls import path
from .views import RegistrationDetail

urlpatterns = [
    path("test/", RegistrationDetail.as_view(), name="test")
]