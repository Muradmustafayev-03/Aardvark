from django.urls import path
from .consumers import QuizConsumer


websocket_urlpatterns = [
    path("", QuizConsumer.as_asgi()),
]
