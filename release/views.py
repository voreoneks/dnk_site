from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse

class MainInfoView(LoginRequiredMixin, FormView):
    template_name = 'release/release.html'
    form_class = MainInfoForm

    def get_redirect_field_name(self) -> str:
        return super().get_redirect_field_name()

    def get_success_url(self) -> str:
        next_url = self.request.POST.get('next', None)
        return next_url

    def get(self, request, *args, **kwargs):
        next = 'single'
        form = self.form_class(initial = {'name': request.user})
        return render(request, self.template_name, {'form': form, 'next': next})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        next = 'single'
        if form.is_valid():
            return HttpResponseRedirect(self.get_success_url())
        return render(request, self.template_name, {'form': form, 'next': next})

    def clean(self):
        cleaned_data = super().clean()

def single(request):
    return render(request, 'release/single.html')