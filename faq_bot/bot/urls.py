from django.urls import path
from .views import bot_view

urlpatterns = [
    path('api/chat/', bot_view, name='bot_view'),
]
