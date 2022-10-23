from django.urls import path
from .views import HomeView, login_view, MemberInfoView



urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('login/', login_view, name='login_view'),
    path('member/info', MemberInfoView.as_view(), name='member_info_view'),    
]
