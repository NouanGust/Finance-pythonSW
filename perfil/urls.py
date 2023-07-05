from django.urls import path
from . import views # O '.' indica a pasta atual

urlpatterns = [
    path('home/', views.home, name="home")
]