from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import NumberAPI, Display

urlpatterns = [
    path('num_to_english', csrf_exempt(NumberAPI.as_view())),
    path('test', Display.as_view())
]
