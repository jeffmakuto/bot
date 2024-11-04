from django.urls import path
from .views import bot_view

urlpatterns = [
    path('bot/', bot_view, name='bot_view'),
]
