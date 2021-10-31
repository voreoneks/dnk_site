from django.urls import path

from calc.views import calc

urlpatterns = [
    path('', calc, name='calc'),
]