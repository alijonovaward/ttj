from .views import Dashboard
from django.urls import path

urlpatterns = [
    path('', Dashboard.as_view(), name = 'home'),
]