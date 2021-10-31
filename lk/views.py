from django.forms.models import model_to_dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import *
from django.urls.base import reverse


class LkView(LoginRequiredMixin, FormView):
    template_name = 'lk/lk.html'
    form_class = LkForm
    form_title = 'Личный кабинет'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        try:
            object_ = Lk.objects.get(user_id = user.id)
            object_dict = model_to_dict(object_)
            object_dict['user'] = user
            form = self.form_class(initial = object_dict)
        except:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            try:
                Lk.objects.get(user_id = user.id).delete()
            except:
                pass
            form.save()
            return HttpResponseRedirect(reverse('lk_success'))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

def success_page(request):
    return render(request, 'success.html')