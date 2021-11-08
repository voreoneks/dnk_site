import os
from datetime import datetime
from pathlib import Path

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView
from dnk_site.settings import BASE_DIR, MEDIA_URL
from google_drive.google_drive import Drive
from google_sheets import Sheet
from lk.models import Lk

from .forms import *
from .models import *
import shutil


def marketing_to_sheet(user):
    drive = Drive()
    date_time = str(datetime.now())
    all_marketing_sheet = Sheet('Маркетинг!A3:AC3')
    all_marketing_values = tuple()

    new_folder = drive.create_folder('1SDzis3xsoSCG57DDngYWyYVLd41cWj3m', str(user) + '_marketing')

    main_info_marketing = MainInfoMarketing.objects.filter(user_id = user.id)
    main_info_marketing_dict = model_to_dict(*main_info_marketing)
    main_info_marketing_values = (
        date_time, main_info_marketing_dict['songers'], main_info_marketing_dict['release_title'], main_info_marketing_dict['release_type'], main_info_marketing_dict['genre'], main_info_marketing_dict['vk'], main_info_marketing_dict['inst'], main_info_marketing_dict['facebook'], main_info_marketing_dict['youtube'], main_info_marketing_dict['tiktok'], main_info_marketing_dict['other']
    )
    all_marketing_values += main_info_marketing_values
    main_info_marketing.delete()

    marketing = Marketing.objects.filter(user_id = user.id)
    marketing_dict = model_to_dict(*marketing)

    if marketing_dict['photo']:
        photo = Path(str(BASE_DIR) + os.path.join(MEDIA_URL, marketing_dict['photo'].name))
        up_photo = drive.upload_file(new_folder['id'], 'Фото для карточки', photo)['webViewLink']
    else:
        photo = ''

    marketing_values = (
        marketing_dict['positioning'], marketing_dict['where_from'], marketing_dict['affiliation'], marketing_dict['awards'], up_photo, marketing_dict['photo_link'], marketing_dict['inspiration'], marketing_dict['concept'], marketing_dict['guest_artists']
    )
    all_marketing_values += marketing_values
    marketing.delete()

    promo_plan = PromoPlan.objects.filter(user_id = user.id)
    if promo_plan:
        promo_plan_dict = model_to_dict(*promo_plan)
        promo_plan_values = (
            promo_plan_dict['radio'], promo_plan_dict['pressa'], promo_plan_dict['social_crops'], promo_plan_dict['tv'], promo_plan_dict['info'], promo_plan_dict['other'], promo_plan_dict['project_plan'], promo_plan_dict['release_plan']
        )
        promo_plan.delete()
    else:
        promo_plan_values = tuple('' for i in range(8))
    all_marketing_values += promo_plan_values


    press_release = PressRelease.objects.filter(user_id = user.id)
    press_release_dict = model_to_dict(*press_release)
    press_release_values = (
        press_release_dict['press_release'],
    )
    all_marketing_values += press_release_values
    press_release.delete()

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

    # folder_path = Path(str(BASE_DIR) + os.path.join(MEDIA_URL, 'uploads/'))
    # shutil.rmtree(folder_path)



class MainInfoMarketingView(LoginRequiredMixin, FormView):
    template_name = 'marketing/marketing.html'
    form_class = MainInfoMarketingForm
    form_title = 'Главная информация'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        main_info = MainInfoMarketing.objects.filter(user_id = user.id)
        if main_info:
            main_info_dict = model_to_dict(*main_info)
            form = self.form_class(initial = main_info_dict)
        else:
            lk = Lk.objects.filter(user_id = user.id)

            if lk:
                lk_dict = model_to_dict(*lk)
                name = lk_dict['name']
                vk = lk_dict['vk']
                inst = lk_dict['inst']
                facebook = lk_dict['facebook']
                youtube = lk_dict['youtube']
                tiktok = lk_dict['tiktok']
                other = lk_dict['telegram']
            else:
                name = ''
                vk = ''
                inst = ''
                facebook = ''
                youtube = ''
                tiktok = ''
                other = ''

            form = self.form_class(initial = {'user': user,
                                              'songers': name,
                                              'vk': vk,
                                              'inst': inst,
                                              'facebook': facebook,
                                              'youtube': youtube,
                                              'tiktok': tiktok,
                                              'other': other})
        return render(request, self.template_name, {'form': form, 
                                                    'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            main_info = MainInfoMarketing.objects.filter(user_id = user.id)
            if main_info:
                main_info.delete()
            form.save()
            return HttpResponseRedirect('marketing_info')
        else:
            return render(request, self.template_name, {'form': form, 
                                                        'form_title': self.form_title})


class MarketingView(LoginRequiredMixin, FormView):
    template_name = 'marketing/marketing_info.html'
    form_class = MarketingForm
    form_title = 'Маркетинг'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        marketing = Marketing.objects.filter(user_id = user.id)
        if marketing:
            marketing_dict = model_to_dict(*marketing)
            photo = marketing_dict['photo']
            form = self.form_class(initial = marketing_dict)
        else:
            photo = ''
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 
                                                    'form_title': self.form_title, 
                                                    'photo': photo, 
                                                    'delete_photo': 'delete_photo'})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            marketing = Marketing.objects.filter(user_id = user.id)
            if marketing:
                marketing_dict = model_to_dict(*marketing)
                photo = marketing_dict['photo']
                marketing.delete()
                forma = form.save(commit = False)
                if photo:
                    forma.photo = photo
                forma.save()
            else:
                form.save()
            return HttpResponseRedirect(reverse('promo_plan'))
        else:
            marketing = Marketing.objects.filter(user_id = user.id)
            if marketing:
                marketing_dict = model_to_dict(*marketing)
                photo = marketing_dict['photo']
            else:
                photo = ''
            return render(request, self.template_name, {'form': form, 
                                                        'form_title': self.form_title, 
                                                        'photo': photo, 
                                                        'delete_photo': 'delete_photo'})


class PromoPlanView(LoginRequiredMixin, FormView):
    template_name = 'marketing/promo_plan.html'
    form_class = PromoPlanForm
    form_title = 'Промо-план'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        promo_plan = PromoPlan.objects.filter(user_id = user.id)
        if promo_plan:
            promo_plan_dict = model_to_dict(*promo_plan)
            promo_plan_dict['user'] = user
            form = self.form_class(initial = promo_plan_dict)
        else:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 
                                                    'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            promo_plan = PromoPlan.objects.filter(user_id = user.id)
            if promo_plan:
                promo_plan.delete()
            form.save()
            return HttpResponseRedirect(reverse('press_release'))
        else:
            return render(request, self.template_name, {'form': form, 
                                                        'form_title': self.form_title})


class PressReleaseView(LoginRequiredMixin, FormView):
    template_name = 'marketing/press_release.html'
    form_class = PressReleaseForm
    form_title = 'Пресс-релиз'
    form_description = '<p>Пресс-релиз обычно состоит из двух абзацев.<br> Первый абзац – несколько предложений об артисте, второй абзац – о песне.</p> <p>Пример: Исполнитель Элджей, ставший известным благодаря вирусной композиции «Розовое вино», выпустил новый трек под названием «Минимал».</p> <p>Песня действительно получилась минималистичной. А рассказывает она о едва различимых и сложно раскрывающихся чувствах к противоположному полу среди молодежи. Во всяком случае, так утверждают поклонники артиста. Как бы там ни было,в тексте присутствует ненормативная лексика. Поэтому,будьте к этому готовы, если решите послушать трек.</p>'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        press_release = PressRelease.objects.filter(user_id = user.id)
        if press_release:
            press_release_dict = model_to_dict(*press_release)
            press_release_dict['user'] = user
            form = self.form_class(initial = press_release)
        else:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 
                                                    'form_title': self.form_title, 
                                                    'form_description': self.form_description})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            press_release = PressRelease.objects.filter(user_id = user.id)
            if press_release:
                press_release.delete()
            form.save()
            marketing_to_sheet(user)
            return HttpResponseRedirect(reverse('m_success'))
        else:
            return render(request, self.template_name, {'form': form, 
                                                        'form_title': self.form_title, 
                                                        'form_description': self.form_description})

def delete_photo(request):
    user = User.objects.get(username = request.user)
    Marketing.objects.filter(user_id = user.id).update(photo = '')
    return HttpResponseRedirect(reverse('marketing_info'))

def success_page(request):
    return render(request, 'success.html')
