from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView

from .forms import *


class LkView(LoginRequiredMixin, FormView):
    template_name = 'lk/lk.html'
    form_class = LkForm
    form_title = 'Личный кабинет'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        lk = Lk.objects.filter(user_id = user.id)
        if lk:
            lk_dict = model_to_dict(*lk)
            lk_dict['user'] = user
            form = self.form_class(initial = lk_dict)
        else:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            lk = Lk.objects.filter(user_id = user.id)
            if lk:
                lk.delete()
            form.save()
            return HttpResponseRedirect(reverse('lk_success'))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

def success_page(request):
    return render(request, 'success.html')
