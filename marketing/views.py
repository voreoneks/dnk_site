from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView

from .forms import *
from .models import *


class MainInfoMarketingView(LoginRequiredMixin, FormView):
    template_name = 'marketing/marketing.html'
    form_class = MainInfoMarketingForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        try:
            objects = MainInfoMarketing.objects.filter(user_id = user.id).values()
            for item in objects:
                data = item
            data['user'] = user
            form = self.form_class(initial = data)
        except:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            try:
                objects = MainInfoMarketing.objects.filter(user_id = user.id)
                for item in objects:
                    item.delete()
            except:
                pass
            form.save()
            return HttpResponseRedirect('marketing_info')
        else:
            return render(request, self.template_name, {'form': form})


class MarketingView(LoginRequiredMixin, FormView):
    template_name = 'marketing/marketing_info.html'
    form_class = MarketingForm
    form_title = 'Маркетинг'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        try:
            objects = Marketing.objects.filter(user_id = user.id).values()
            for item in objects:
                data = item
            data['user'] = user
            form = self.form_class(initial = data)
        except:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            try:
                objects = Marketing.objects.filter(user_id = user.id)
                for item in objects:
                    item.delete()
            except:
                pass
            form.save()
            return HttpResponseRedirect(reverse('promo_plan'))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})


class PromoPlanView(LoginRequiredMixin, FormView):
    template_name = 'marketing/promo_plan.html'
    form_class = PromoPlanForm
    form_title = 'Промо-план'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        try:
            objects = PromoPlan.objects.filter(user_id = user.id).values()
            for item in objects:
                data = item
            data['user'] = user
            form = self.form_class(initial = data)
        except:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            try:
                objects = PromoPlan.objects.filter(user_id = user.id)
                for item in objects:
                    item.delete()
            except:
                pass
            form.save()
            return HttpResponseRedirect(reverse('press_release'))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})


class PressReleaseView(LoginRequiredMixin, FormView):
    template_name = 'marketing/press_release.html'
    form_class = PressReleaseForm
    form_title = 'Пресс-релиз'
    form_description = '<p>Пресс-релиз обычно состоит из двух абзацев.<br> Первый абзац – несколько предложений об артисте, второй абзац – о песне.</p> <p>Пример: Исполнитель Элджей, ставший известным благодаря вирусной композиции «Розовое вино», выпустил новый трек под названием «Минимал».</p> <p>Песня действительно получилась минималистичной. А рассказывает она о едва различимых и сложно раскрывающихся чувствах к противоположному полу среди молодежи. Во всяком случае, так утверждают поклонники артиста. Как бы там ни было,в тексте присутствует ненормативная лексика. Поэтому,будьте к этому готовы, если решите послушать трек.</p>'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        try:
            objects = PressRelease.objects.filter(user_id = user.id).values()
            for item in objects:
                data = item
            data['user'] = user
            form = self.form_class(initial = data)
        except:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            try:
                objects = PressRelease.objects.filter(user_id = user.id)
                for item in objects:
                    item.delete()
            except:
                pass
            form.save()
            return HttpResponseRedirect(reverse('m_success'))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})

def success_page(request):
    return render(request, 'success.html')
