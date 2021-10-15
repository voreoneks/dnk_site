from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.forms import formset_factory

from .forms import *
from .models import *


class MainInfoView(LoginRequiredMixin, FormView):
    template_name = 'release/release.html'
    form_class = MainInfoForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        try:
            main_info = MainInfo.objects.filter(user_id = user.id).values()
            for item in main_info:
                main = item
            main['user'] = user
            form = self.form_class(initial = main)
        except:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        print(request.POST)
        if form.is_valid():
            try:
                main_info = MainInfo.objects.filter(user_id = user.id)
                for item in main_info:
                    item.delete()
            except:
                pass
            form.save()
            if form.cleaned_data['content_type'] == 'SINGLE' or form.cleaned_data['content_type'] == 'ALBUM':
                self.next = 'audio'
            else:
                self.next = 'video'
            return HttpResponseRedirect(self.next + '?c=' + form.cleaned_data['content_type'])
        else:
            return render(request, self.template_name, {'form': form})


class AudioView(LoginRequiredMixin, FormView):
    template_name = 'release/audio.html'
    form_class = AudioForm
    def get(self, request, *args, **kwargs):
        fields_for_button = ['songers', 'song_title', 'album_title', 'feat', 'genre', 'fio_songer', 'words_author', 'music_author', 'owner_citizenship', 'record_country', 'timing', 'song_preview', 'lexis', 'audio_link', 'clean_link', 'release_year', 'add_video']
        content_type = request.POST.get('c', False)
        user = User.objects.get(username = request.user)
        num_songs = MainInfo.objects.get(user_id = user.id).num_songs
        audio_formset = formset_factory(self.form_class, extra=num_songs)
        formset = audio_formset()
        return render(request, self.template_name, {'formset': formset, 'button':fields_for_button}) 

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
