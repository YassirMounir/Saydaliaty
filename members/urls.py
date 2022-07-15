from django.urls import path
from .views import UserRegisterview

# URLConfig
urlpatterns = [
    path('register/', UserRegisterview.as_view(), name='signup'),
]
