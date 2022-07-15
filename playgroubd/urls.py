from django.urls import path
from . import views
from .views import UserRegisterView

# URLConfig
urlpatterns = [
    path('', views.home),
    path('signup/', UserRegisterView.as_view(), name='Register'),
    path('signin/', views.signin),
    path('home', views.home),
    # path('products', views.products),
    path('med_search', views.med_search),
    path('profile', views.profile),
]
