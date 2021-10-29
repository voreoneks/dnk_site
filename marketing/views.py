from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.forms.models import model_to_dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView
from datetime import datetime

from google_sheets import Sheet

from .forms import *
from .models import *


def marketing_to_sheet(user):
    date_time = str(datetime.now())
    all_marketing_sheet = Sheet('Маркетинг!A3:AC3')
    all_marketing_values = tuple()

    main_info_marketing = MainInfoMarketing.objects.get(user_id = user.id)
    main_info_marketing_dict = model_to_dict(main_info_marketing)
    main_info_marketing_values = (
        date_time, main_info_marketing_dict['songers'], main_info_marketing_dict['release_title'], main_info_marketing_dict['release_type'], main_info_marketing_dict['genre'], main_info_marketing_dict['vk'], main_info_marketing_dict['inst'], main_info_marketing_dict['facebook'], main_info_marketing_dict['youtube'], main_info_marketing_dict['tiktok'], main_info_marketing_dict['other']
    )
    all_marketing_values += main_info_marketing_values

    marketing = Marketing.objects.get(user_id = user.id)
    marketing_dict = model_to_dict(marketing)
    marketing_values = (
        marketing_dict['positioning'], marketing_dict['where_from'], marketing_dict['affiliation'], marketing_dict['awards'], '', marketing_dict['photo_link'], marketing_dict['inspiration'], marketing_dict['concept'], marketing_dict['guest_artists']
    )
    all_marketing_values += marketing_values

    try:
        promo_plan = PromoPlan.objects.get(user_id = user.id)
        promo_plan_dict = model_to_dict(promo_plan)
        promo_plan_values = (
            promo_plan_dict['radio'], promo_plan_dict['pressa'], promo_plan_dict['social_crops'], promo_plan_dict['tv'], promo_plan_dict['info'], promo_plan_dict['other'], promo_plan_dict['project_plan'], promo_plan_dict['release_plan']
        )
    except:
        promo_plan_values = tuple('' for i in range(8))
    all_marketing_values += promo_plan_values

    press_release = PressRelease.objects.get(user_id = user.id)
    press_release_dict = model_to_dict(press_release)
    press_release_values = (
        press_release_dict['press_release'],
    )
    all_marketing_values += press_release_values

    all_marketing_data = {
        'range': 'Маркетинг!A3:AC3',
        'majorDimension': 'ROWS',
        'values': [all_marketing_values,]
    }

    all_marketing_sheet.append(all_marketing_data)

    spaces = Sheet('Маркетинг!A3:AC3')
    spaces_values = tuple('.' for i in range(29))
    spaces_data = {
        'range': 'Маркетинг!A3:AC3',
        'majorDimension': 'ROWS',
        'values': [spaces_values,]
    }
    spaces.append(spaces_data)


class MainInfoMarketingView(LoginRequiredMixin, FormView):
    template_name = 'marketing/marketing.html'
    form_class = MainInfoMarketingForm
    form_title = 'Главная информация'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        objects = MainInfoMarketing.objects.filter(user_id = user.id).values()
        if len(objects) != 0:
            for item in objects:
                data = item
            data['user'] = user
            form = self.form_class(initial = data)
        else:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            objects = MainInfoMarketing.objects.filter(user_id = user.id)
            if len(objects) != 0:
                for item in objects:
                    item.delete()
            form.save()
            return HttpResponseRedirect('marketing_info')
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})


class MarketingView(LoginRequiredMixin, FormView):
    template_name = 'marketing/marketing_info.html'
    form_class = MarketingForm
    form_title = 'Маркетинг'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        objects = Marketing.objects.filter(user_id = user.id).values()
        if len(objects) != 0:
            for item in objects:
                data = item
            data['user'] = user
            form = self.form_class(initial = data)
        else:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            objects = Marketing.objects.filter(user_id = user.id)
            if len(objects) != 0:
                for item in objects:
                    item.delete()
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
        objects = PromoPlan.objects.filter(user_id = user.id).values()
        if len(objects) != 0:
            for item in objects:
                data = item
            data['user'] = user
            form = self.form_class(initial = data)
        else:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            objects = PromoPlan.objects.filter(user_id = user.id)
            if len(objects) != 0:
                for item in objects:
                    item.delete()
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
        objects = PressRelease.objects.filter(user_id = user.id).values()
        if len(objects) != 0:
            for item in objects:
                data = item
            data['user'] = user
            form = self.form_class(initial = data)
        else:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            objects = PressRelease.objects.filter(user_id = user.id)
            if len(objects) != 0:
                for item in objects:
                    item.delete()
            form.save()
            marketing_to_sheet(user)
            return HttpResponseRedirect(reverse('m_success'))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})

def success_page(request):
    return render(request, 'success.html')
