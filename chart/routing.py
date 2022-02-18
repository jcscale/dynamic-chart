from django.urls import path
from chart.consumers import ChartConsumer

websocket_urlpatterns = [
    path('ws/chart/', ChartConsumer.as_asgi())
]
