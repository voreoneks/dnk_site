from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView
from google_sheets import Sheet
from lk.models import Lk

from .forms import MainInfoMarketingForm
from .models import MainInfoMarketing


def marketing_to_sheet(user):
    date_time = str(datetime.now())
    all_marketing_sheet = Sheet('Маркетинг!A3:M3')
    all_marketing_values = tuple()

    main_info_marketing = MainInfoMarketing.objects.filter(user_id = user.id)
    main_info_marketing_dict = model_to_dict(*main_info_marketing)
    main_info_marketing_values = (
        date_time, main_info_marketing_dict['songers'], main_info_marketing_dict['release_title'], main_info_marketing_dict['vk'], main_info_marketing_dict['inst'], main_info_marketing_dict['facebook'], main_info_marketing_dict['youtube'], main_info_marketing_dict['tiktok'], main_info_marketing_dict['other'], main_info_marketing_dict['focus_track'], main_info_marketing_dict['photo_link'], main_info_marketing_dict['press_release'], main_info_marketing_dict['pr'], 
    )
    all_marketing_values += main_info_marketing_values
    main_info_marketing.delete()

    all_marketing_data = {
        'range': 'Маркетинг!A3:M3',
        'majorDimension': 'ROWS',
        'values': [all_marketing_values,]
    }

    all_marketing_sheet.append(all_marketing_data)

    spaces = Sheet('Маркетинг!A3:M3')
    spaces_values = tuple('.' for i in range(13))
    spaces_data = {
        'range': 'Маркетинг!A3:M3',
        'majorDimension': 'ROWS',
        'values': [spaces_values,]
    }
    spaces.append(spaces_data)


class MainInfoMarketingView(LoginRequiredMixin, FormView):
    template_name = 'marketing/marketing.html'
    form_class = MainInfoMarketingForm
    form_title = 'Трейд-маркетинг'

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
            marketing_to_sheet(user)
            return HttpResponseRedirect(reverse('m_success'))
        else:
            return render(request, self.template_name, {'form': form, 
                                                        'form_title': self.form_title})



def success_page(request):
    return render(request, 'success.html')
