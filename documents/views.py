from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
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

class OrgInfoView(LoginRequiredMixin, FormView):
    template_name = 'documents/orginfo.html'

    def get_form_class(self):
        user = User.objects.get(username = self.request.user)
        you_are = MainInfoDocs.objects.filter(user_id = user.id)[0].you_are
        if you_are == 'IPRF':
            return OrgInfoIprfForm
        elif you_are == 'IPIN':
            return OrgInfoIpinForm
        elif you_are == 'SAM':
            return OrgInfoSamForm
        else: 
            return OrgInfoOooForm

    def get_model(self):
        user = User.objects.get(username = self.request.user)
        you_are = MainInfoDocs.objects.filter(user_id = user.id)[0].you_are
        if you_are == 'IPRF':
            return OrgInfoIprf
        elif you_are == 'IPIN':
            return OrgInfoIpin
        elif you_are == 'SAM':
            return OrgInfoSam
        else: 
            return OrgInfoOoo


    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = self.request.user)
        org_info = self.get_model().objects.filter(user_id = user.id).values()
        self.form_class = self.get_form_class()
        if len(org_info) != 0:
            for item in org_info:
                data = item
            data['user'] = user
            form = self.form_class(initial = data)
        else:
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            org_info = self.get_model().objects.filter(user_id = user.id)
            if len(org_info) != 0:
                for item in org_info:
                    item.delete()
            form.save()
            return HttpResponseRedirect(reverse('choice', args=[1]))
        else:
            return render(request, self.template_name, {'form': form})

    

def choice(request, id):
    if request.method == 'GET':
        context = dict()
        if id == 1:
            form = '<ul id="id_content_type"><li><label for="id_content_type_0"><input type="radio" name="choice" value="SINGLE" required id="id_content_type_0">Сингл</label></li><li><label for="id_content_type_1"><input type="radio" name="choice" value="ALBUM" required id="id_content_type_1" checked>Альбом</label></li><li><label for="id_content_type_2"><input type="radio" name="choice" value="CLIP" required id="id_content_type_2">Видеоклип</label></li></ul>'
            context = {
                'form_title': 'Тип релиза',
                'form': form,
            }
        elif id == 2:
            form = '<ul id="id_music_author"><li><label for="id_music_author_0"><input type="radio" name="music_author" value="CITIZEN" required id="id_music_author_0">Гражданин РФ</label></li><li><label for="id_music_author_1"><input type="radio" name="music_author" value="FOREIGN" required id="id_music_author_1" checked>Иностранный гражданин</label></li></ul>'
            context = {
                'form_title': 'Автор музыки',
                'form': form,
            }
        return render(request, 'documents/choice.html', context)
    else:
        choice = request.POST.get('choice')
        if choice == 'SINGLE' or choice == 'ALBUM':
            return HttpResponseRedirect(reverse('audio'))
        elif choice == 'CLIP':
            return HttpResponseRedirect(reverse('video'))
        elif choice == 'CITIZEN':
            return HttpResponseRedirect(reverse('music_author_citizen'))
        elif choice == 'FOREIGN':
            return HttpResponseRedirect(reverse('music_author_foreign'))

class AudioDocsView(LoginRequiredMixin, FormView):
    template_name = 'documents/audio.html'
    form_class = AudioDocsForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        num_songs = MainInfoDocs.objects.get(user_id = user.id).num_songs
        audio_formset = formset_factory(self.form_class)
        data = {
            'form-TOTAL_FORMS': str(num_songs),
            'form-INITIAL_FORMS': str(num_songs),
        }
        audio = AudioDocs.objects.filter(user_id = user.id)
        if len(audio) != 0:
            for song in range(len(audio)):
                for field in AudioDocsForm._meta.fields:
                    data['form-' + str(song) + '-' + field] = getattr(audio[song], field)
        else:
            for num in range(num_songs):
                data['form-' + str(num) + '-user'] = user.id
        formset = audio_formset(data)
        return render(request, self.template_name, {'button': self.form_class._meta.fields, 'formset': formset})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        audio_formset = formset_factory(self.form_class)
        formset = audio_formset(data = self.request.POST, files = self.request.FILES)
        add_video = self.request.POST.get('add_video')
        print(formset.errors)
        if formset.is_valid():
            try:
                audio = AudioDocs.objects.filter(user_id = user.id)
                for song in audio:
                    song.delete()
            except:
                pass
            for form in formset:
                form.save()
            if add_video == 'NO':
                return HttpResponseRedirect(reverse('licence'))
            else:
                return HttpResponseRedirect(reverse('video'))
        else:
            return render(request, self.template_name, {'button': self.form_class._meta.fields, 'formset': formset})


class VideoDocsView(LoginRequiredMixin, FormView):
    template_name = 'documents/video.html'
    form_class = VideoDocsForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        video = VideoDocs.objects.filter(user_id = user.id).values()
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
            video = VideoDocs.objects.filter(user_id = user.id)
            if len(video) != 0:
                for item in video:
                    item.delete()
            form.save()
            return HttpResponseRedirect(reverse('licence'))
        else:
            return render(request, self.template_name, {'form': form})


class LicenceView(LoginRequiredMixin, FormView):
    template_name = 'documents/licence.html'
    form_class = LicenceForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        licence = Licence.objects.filter(user_id = user.id).values()
        if len(licence) != 0:
            for item in licence:
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
            licence = Licence.objects.filter(user_id = user.id)
            if len(licence) != 0:
                for item in licence:
                    item.delete()
            form.save()
            return HttpResponseRedirect(reverse('choice', args=[2]))
        else:
            return render(request, self.template_name, {'form': form})


