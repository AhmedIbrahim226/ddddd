from django.urls import path
from .views import TenantRetrieveAPI

urlpatterns = [
    path('retrieve/', TenantRetrieveAPI.as_view()),
]