from django.urls import path
from .views import MemberInfoView


urlpatterns = [
    path('', MemberInfoView.as_view(), name='member_info'),
]
