from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import NumberAPI

urlpatterns = [
    path('', csrf_exempt(NumberAPI.as_view()))
]
