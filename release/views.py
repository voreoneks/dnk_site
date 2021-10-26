from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.forms.models import model_to_dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView
from google_sheets import Sheet

from .forms import *
from .models import *

def release_to_sheet(user):
    date_time = str(datetime.now())
    release_sheet = Sheet('A3:AM3')

    main_info = MainInfo.objects.get(user_id = user.id)
    main_info_dict = model_to_dict(main_info)
    content_type = main_info_dict['content_type']
    audio = Audio.objects.filter(user_id = user.id)
    audio_tuple_dict = tuple(model_to_dict(item) for item in audio)
    video = Video.objects.get(user_id = user.id)
    video_dict = model_to_dict(video)
    release_values = tuple()

    main_info_values = (
        date_time, main_info_dict['name'], main_info_dict['content_type'], main_info_dict['phone_number'], main_info_dict['email'], main_info_dict['is_update_photo'], main_info_dict['photo_link']
    )
    release_values += main_info_values

    try:
        audio_values = (
            audio_tuple_dict[0]['songers'], audio_tuple_dict[0]['song_title'], audio_tuple_dict[0]['album_title'], audio_tuple_dict[0]['feat'], audio_tuple_dict[0]['genre'], audio_tuple_dict[0]['fio_songer'], audio_tuple_dict[0]['words_author'], audio_tuple_dict[0]['music_author'], audio_tuple_dict[0]['owner_citizenship'], audio_tuple_dict[0]['record_country'], audio_tuple_dict[0]['timing'], audio_tuple_dict[0]['song_preview'], audio_tuple_dict[0]['lexis'], '', '', audio_tuple_dict[0]['audio_link'], '', audio_tuple_dict[0]['clean_link'], '', audio_tuple_dict[0]['release_year']
        )
    except:
        audio_values = tuple('' for i in range(20))
    
    release_values += audio_values

    try:
        video_values = (
            video_dict['songers'], video_dict['video_title'], video_dict['feat'], video_dict['words_author'], video_dict['music_author'], video_dict['lexis'], video_dict['director'], video_dict['timing'], video_dict['release_year'], video_dict['video_link'], '', video_dict['production_country']
        )
    except:
        release_values = tuple('' for i in range(12))
        
    release_values += video_values

    release_data = {
            'range': 'A3:AM3',
            'majorDimension': 'ROWS',
            'values': [release_values,]
        }
    release_sheet.append(release_data)

    try:
        add_audio_sheet = Sheet('A3:AM3')
        add_audio_values = []
        for i in range(1, len(audio_tuple_dict)):
            add_audio_values.append(tuple(('', '',  '',  '',  '',  '',  '', audio_tuple_dict[i]['songers'], audio_tuple_dict[i]['song_title'], audio_tuple_dict[i]['album_title'], audio_tuple_dict[i]['feat'], audio_tuple_dict[i]['genre'], audio_tuple_dict[i]['fio_songer'], audio_tuple_dict[i]['words_author'], audio_tuple_dict[i]['music_author'], audio_tuple_dict[i]['owner_citizenship'], audio_tuple_dict[i]['record_country'], audio_tuple_dict[i]['timing'], audio_tuple_dict[i]['song_preview'], audio_tuple_dict[i]['lexis'], '', '', audio_tuple_dict[i]['audio_link'], '', audio_tuple_dict[i]['clean_link'], '', audio_tuple_dict[i]['release_year'])))

        add_audio_data = {
            'range': 'A3:AM3',
            'majorDimension': 'ROWS',
            'values': add_audio_values
            }
        add_audio_sheet.append(add_audio_data)
    except:
        pass

    spaces = Sheet('A3:AM3')
    spaces_values = [tuple('.' for i in range(39))]
    spaces_data = {
        'range': 'A3:AM3',
        'majorDimension': 'ROWS',
        'values': spaces_values
    }
    spaces.append(spaces_data)
    main_info.delete()
    for item in audio:
        item.delete()
    video.delete()


class MainInfoView(LoginRequiredMixin, FormView):
    template_name = 'release/release.html'
    form_class = MainInfoForm
    form_title = 'Главная информация'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        try:
            main_info = MainInfo.objects.filter(user_id = user.id).values()
            for item in main_info:
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
                main_info = MainInfo.objects.filter(user_id = user.id)
                for item in main_info:
                    item.delete()
            except:
                pass
            form.save()
            if form.cleaned_data['content_type'] == 'SINGLE' or form.cleaned_data['content_type'] == 'ALBUM':
                self.next = 'r_audio'
            else:
                self.next = 'r_video'
            return HttpResponseRedirect(reverse(self.next))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})


class AudioView(LoginRequiredMixin, FormView):
    template_name = 'release/audio.html'
    form_class = AudioForm
    form_title = 'Аудио'
    fields_for_button = ['songers', 'song_title', 'album_title', 'feat', 'genre', 'fio_songer', 'words_author', 'music_author', 'owner_citizenship', 'record_country', 'timing', 'song_preview', 'lexis', 'audio_link', 'clean_link', 'release_year', 'add_video',]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        num_songs = MainInfo.objects.get(user_id = user.id).num_songs
        audio_formset = formset_factory(self.form_class)
        data = {
            'form-TOTAL_FORMS': str(num_songs),
            'form-INITIAL_FORMS': str(num_songs),
        }
        try:
            audio = Audio.objects.filter(user_id = user.id)
            for song in range(len(audio)):
                for field in AudioForm._meta.fields:
                    data['form-' + str(song) + '-' + field] = getattr(audio[song], field)
        except:
            for num in range(num_songs):
                data['form-' + str(num) + '-user'] = user.id
        formset = audio_formset(data)
        return render(request, self.template_name, {'button': self.fields_for_button, 'formset': formset, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        audio_formset = formset_factory(self.form_class)
        formset = audio_formset(data = self.request.POST, files = self.request.FILES)
        add_video = self.request.POST.get('add_video')
        if formset.is_valid():
            try:
                audio = Audio.objects.filter(user_id = user.id)
                for song in audio:
                    song.delete()
            except:
                pass
            for form in formset:
                form.save()
            if add_video == 'NO':
                release_to_sheet(user)
                return HttpResponseRedirect(reverse('r_success'))
            else:
                return HttpResponseRedirect(reverse('r_video'))
        else:
            return render(request, self.template_name, {'button': self.fields_for_button, 'formset': formset, 'form_title': self.form_title})


class VideoView(LoginRequiredMixin, FormView):
    template_name = 'release/video.html'
    form_class = VideoForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        try:
            video = Video.objects.filter(user_id = user.id).values()
            for item in video:
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
                video = Video.objects.filter(user_id = user.id)
                for item in video:
                    item.delete()
            except:
                pass
            form.save()
            release_to_sheet(user)
            return HttpResponseRedirect(reverse('r_success'))
        else:
            return render(request, self.template_name, {'form': form})

            

def success_page(request):
    return render(request, 'success.html')
