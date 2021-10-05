from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import *

def MainPage(request):
    return render(request, 'main.html')

class LogoutPage(LogoutView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Выход из системы'
        return context

class NewsPage(ListView):
    template_name = 'news.html'
    context_object_name = 'news'

    def get_queryset(self):
        news = News.objects.filter(user_visible__username = self.request.user)
        return news

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DNK Music'
        return context 
    