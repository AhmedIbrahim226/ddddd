from django.urls import path
from .views import HomeView, LoginView, MemberInfoView



urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('member/info', MemberInfoView.as_view(), name='member_info_view'),    
]
