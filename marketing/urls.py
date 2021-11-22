from django.urls import path
from .views import MainInfoMarketingView, success_page

urlpatterns = [
    path('', MainInfoMarketingView.as_view(), name='marketing'),
    path('success/', success_page, name='m_success'),
]