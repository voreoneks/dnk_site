from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.urls.base import reverse
from dnk_site.settings import BASE_DIR
import os
from pathlib import Path

from .models import *

def MainPage(request):
    return render(request, 'main.html')

class LogoutPage(LogoutView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Выход из системы'
        return context

class NewsPage(ListView):
    template_name = 'news/news.html'
    context_object_name = 'news'

    def get_queryset(self):
        news = News.objects.filter(user_visible__username = self.request.user)
        return news

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DNK Music'
        return context 
    
def download(request, slug_):
    news = News.objects.get(slug = slug_)
    file_path = str(Path(__file__).parent.parent) + str(Path(news.file.url)) 
    filename = str(Path(file_path).name)

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read())
        response['Content-Type'] = 'text/plain'
        response['Content-Disposition'] = 'attachment; filename=' + filename
    return response