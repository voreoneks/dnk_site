from django.urls import path
from .views import *
from marketing.models import MainInfoMarketing

urlpatterns = [
    path('', MainInfoMarketingView.as_view(), name='marketing'),
    path('marketing_info/', MarketingView.as_view(), name='marketing_info'),
    path('promo_plan/', PromoPlanView.as_view(), name='promo_plan'),
    path('success/', success_page, name='success'),
]