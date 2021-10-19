from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import FormView

from .forms import *
from .models import *


class MainInfoView(LoginRequiredMixin, FormView):
    template_name = 'release/release.html'
    form_class = MainInfoForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        main_info = MainInfo.objects.filter(user_id = user.id).values()
        if len(main_info) != 0:
            for item in main_info:
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
            main_info = MainInfo.objects.filter(user_id = user.id)
            if len(main_info) != 0:
                for item in main_info:
                    item.delete()
            form.save()
            if form.cleaned_data['content_type'] == 'SINGLE' or form.cleaned_data['content_type'] == 'ALBUM':
                self.next = 'audio'
            else:
                self.next = 'video'
            return HttpResponseRedirect(self.next)
        else:
            return render(request, self.template_name, {'form': form})


class AudioView(LoginRequiredMixin, FormView):
    template_name = 'release/audio.html'
    form_class = AudioForm
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
        return render(request, self.template_name, {'button': self.fields_for_button, 'formset': formset})

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
                return HttpResponseRedirect(reverse_lazy('success'))
            else:
                return HttpResponseRedirect(reverse_lazy('video'))
        else:
            return render(request, self.template_name, {'button': self.fields_for_button, 'formset': formset})


class VideoView(LoginRequiredMixin, FormView):
    template_name = 'release/video.html'
    form_class = VideoForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        video = Video.objects.filter(user_id = user.id).values()
        if len(video) != 0:
            for item in video:
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
            video = Video.objects.filter(user_id = user.id)
            if len(video) != 0:
                for item in video:
                    item.delete()
            form.save()
            return HttpResponseRedirect(reverse_lazy('success'))
        else:
            return render(request, self.template_name, {'form': form})

            

def success_page(request):
    return render(request, 'release/success.html')
