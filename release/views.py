from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *

class MainInfoView(LoginRequiredMixin, FormView):
    template_name = 'release.html'
    form_class = MainInfoForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
