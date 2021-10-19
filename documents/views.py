from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import FormView

from .forms import *
from .models import *


class MainInfoDocsView(LoginRequiredMixin, FormView):
    template_name = 'documents/documents.html'
    form_class = MainInfoDocsForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        main_info_docs = MainInfoDocs.objects.filter(user_id = user.id).values()
        if len(main_info_docs) != 0:
            for item in main_info_docs:
                data = item
            data['user'] = user
            form = self.form_class(initial = data)
        else:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            main_info_docs = MainInfoDocs.objects.filter(user_id = user.id)
            if len(main_info_docs) != 0:
                for item in main_info_docs:
                    item.delete()
            form.save()
            return HttpResponseRedirect('orginfo')
        else:
            return render(request, self.template_name, {'form': form})

