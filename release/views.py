import os
from datetime import datetime
from pathlib import Path
from django import http

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.forms.models import model_to_dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView
from dnk_site.settings import BASE_DIR, MEDIA_URL, MEDIA_ROOT
from google_drive.google_drive import Drive
from google_sheets import Sheet
from lk.models import *
from silk.profiling.profiler import silk_profile

from .forms import *
from .models import *


def release_to_cloud(user):
    drive = Drive()
    date_time = str(datetime.now())
    release_sheet = Sheet('Релиз!A3:AO3')

    main_info = MainInfo.objects.filter(user_id = user.id)
    main_info_dict = model_to_dict(main_info[0])
    release_values = tuple()

    new_folder = drive.create_folder('1SDzis3xsoSCG57DDngYWyYVLd41cWj3m', str(user) + '_release')

    if main_info_dict['photo']:
        photo = str(BASE_DIR) + os.path.join(MEDIA_URL, main_info_dict['photo'].name)
        up_photo = drive.upload_file(new_folder['id'], 'Фото для карточки', photo)['webViewLink']
    else: 
        up_photo = ''
    if main_info_dict['cover']:
        cover = str(BASE_DIR) + os.path.join(MEDIA_URL, main_info_dict['cover'].name)
        up_cover = drive.upload_file(new_folder['id'], 'Обложка', cover)['webViewLink']
    else:
        up_cover = ''
    if main_info_dict['cover_psd']:
        cover_psd = str(BASE_DIR) + os.path.join(MEDIA_URL, main_info_dict['cover_psd'].name)
        up_cover_psd = drive.upload_file(new_folder['id'], 'Обложка_PSD', cover_psd)['webViewLink']
    else:
        up_cover_psd = ''


    main_info_values = (
        date_time, main_info_dict['name'], main_info_dict['content_type'], main_info_dict['phone_number'], main_info_dict['email'], main_info_dict['is_update_photo'], main_info_dict['photo_link'], up_photo, up_cover, up_cover_psd
    )
    release_values += main_info_values
    main_info.delete()


    audio = Audio.objects.filter(user_id = user.id)
    if audio:
        audio_tuple_dict = tuple(model_to_dict(item) for item in audio)
        up_song_tuple = tuple()
        up_clean_link_tuple = tuple()
        up_instrumental_tuple = tuple()
        up_song_text_tuple = tuple()

        for item in audio_tuple_dict:

            if item['audio']:
                song = str(BASE_DIR) + os.path.join(MEDIA_URL, item['audio'].name)
                up_song = drive.upload_file(new_folder['id'], item['song_title'], song)['webViewLink']
            else:
                up_song = ''
            up_song_tuple = (*up_song_tuple, up_song)

            if item['clean_link']:
                clean_link = str(BASE_DIR) + os.path.join(MEDIA_URL, item['clean_link'].name)
                up_clean_link = drive.upload_file(new_folder['id'], item['song_title'] + '_clean', clean_link)['webViewLink']
            else:
                up_clean_link = ''
            up_clean_link_tuple = (*up_clean_link_tuple, up_clean_link)

            if item['instrumental']:
                instrumental = str(BASE_DIR) + os.path.join(MEDIA_URL, item['instrumental'].name)
                up_instrumental = drive.upload_file(new_folder['id'], item['song_title'] + '_instrumental', instrumental)['webViewLink']
            else:
                up_instrumental = ''
            up_instrumental_tuple = (*up_instrumental_tuple, up_instrumental)

            if item['song_text']:
                song_text = str(BASE_DIR) + os.path.join(MEDIA_URL, item['song_text'].name)
                up_song_text = drive.upload_file(new_folder['id'], item['song_title'] + '_text', song_text)['webViewLink']
            else:
                up_song_text = ''
            up_song_text_tuple = (*up_song_text_tuple, up_song_text)

        audio_values = (
            audio_tuple_dict[0]['songers'], audio_tuple_dict[0]['song_title'], audio_tuple_dict[0]['album_title'], audio_tuple_dict[0]['feat'], audio_tuple_dict[0]['genre'], audio_tuple_dict[0]['fio_songer'], audio_tuple_dict[0]['words_author'], audio_tuple_dict[0]['music_author'], audio_tuple_dict[0]['owner_citizenship'], audio_tuple_dict[0]['record_country'], audio_tuple_dict[0]['timing'], audio_tuple_dict[0]['song_preview'], audio_tuple_dict[0]['lexis'], audio_tuple_dict[0]['audio_link'], up_song_tuple[0], up_clean_link_tuple[0], up_instrumental_tuple[0], up_song_text_tuple[0], audio_tuple_dict[0]['release_year']
        )

    else:
        audio_values = tuple('' for i in range(20))
    
    release_values += audio_values

    video = Video.objects.filter(user_id = user.id)
    if video:
        video_dict = model_to_dict(video[0])
        if video_dict['video_preview']:
            video_preview = str(BASE_DIR) + os.path.join(MEDIA_URL, video_dict['video_preview'].name)
            up_video_preview = drive.upload_file(new_folder['id'], 'Превью видео', video_preview)['webViewLink']
        video_values = (
            video_dict['songers'], video_dict['video_title'], video_dict['feat'], video_dict['words_author'], video_dict['music_author'], video_dict['lexis'], video_dict['director'], video_dict['timing'], video_dict['release_year'], video_dict['video_link'], up_video_preview, video_dict['production_country']
        )
        video.delete()
    else:
        video_values = tuple('' for i in range(12))
        
    release_values += video_values

    release_data = {
            'range': 'Релиз!A3:AO3',
            'majorDimension': 'ROWS',
            'values': [release_values,]
        }
    release_sheet.append(release_data)

    if len(audio) > 1:
        add_audio_sheet = Sheet('Релиз!A3:AO3')
        add_audio_values = []
        for i in range(1, len(audio_tuple_dict)):
            add_audio_values.append(tuple(('', '',  '',  '',  '',  '',  '', '', '', '', audio_tuple_dict[i]['songers'], audio_tuple_dict[i]['song_title'], audio_tuple_dict[i]['album_title'], audio_tuple_dict[i]['feat'], audio_tuple_dict[i]['genre'], audio_tuple_dict[i]['fio_songer'], audio_tuple_dict[i]['words_author'], audio_tuple_dict[i]['music_author'], audio_tuple_dict[i]['owner_citizenship'], audio_tuple_dict[i]['record_country'], audio_tuple_dict[i]['timing'], audio_tuple_dict[i]['song_preview'], audio_tuple_dict[i]['lexis'], audio_tuple_dict[i]['audio_link'], up_song_tuple[i], up_clean_link_tuple[i], up_instrumental_tuple[i], up_song_text_tuple[i], audio_tuple_dict[i]['release_year'])))

        add_audio_data = {
            'range': 'Релиз!A3:AO3',
            'majorDimension': 'ROWS',
            'values': add_audio_values
            }
        add_audio_sheet.append(add_audio_data)
        

    spaces = Sheet('Релиз!A3:AO3')
    spaces_values = [tuple('.' for i in range(41))]
    spaces_data = {
        'range': 'Релиз!A3:AO3',
        'majorDimension': 'ROWS',
        'values': spaces_values
    }
    spaces.append(spaces_data)

    if audio:
         audio.delete()
    

class MainInfoView(LoginRequiredMixin, FormView):
    template_name = 'release/release.html'
    form_class = MainInfoForm
    form_title = 'Главная информация'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        main_info = MainInfo.objects.filter(user_id = user.id)

        if main_info:
            main_info_dict = model_to_dict(*main_info)
            photo = main_info_dict['photo']
            cover = main_info_dict['cover']
            if main_info_dict['cover_psd']:
                cover_psd = Path(main_info_dict['cover_psd'].name).name
            else:
                cover_psd = ''
            form = self.form_class(initial = main_info_dict)
        else:
            lk = Lk.objects.filter(user_id = user.id)

            if lk:
                lk_dict = model_to_dict(*lk)
                name = lk_dict['name']
                phone = lk_dict['phone']
                email = lk_dict['email']
            else:
                name = ''
                phone = ''
                email = ''

            photo = ''
            cover = ''
            cover_psd = ''
            form = self.form_class(initial = {'name': name, 
                                              'phone_number': phone, 
                                              'email': email, 
                                              'user': user})
        return render(request, self.template_name, 
                    {'form': form, 
                    'form_title': self.form_title, 
                    'photo': photo, 
                    'cover': cover, 
                    'cover_psd': cover_psd})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            main_info = MainInfo.objects.filter(user_id = user.id)

            if main_info:
                main_info_dict = model_to_dict(*main_info)
                photo = main_info_dict['photo']
                cover = main_info_dict['cover']
                cover_psd = main_info_dict['cover_psd']
                main_info.delete()
                forma = form.save(commit = False)
                if request.FILES.get('cover') == None and cover:
                    forma.cover = cover
                if request.FILES.get('photo') == None and photo:
                    forma.photo = photo
                if request.FILES.get('cover_psd') == None and cover_psd:
                    forma.cover_psd = cover_psd
                forma.save()
            else:
                form.save()

            audio = Audio.objects.filter(user_id = user.id)
            if audio:
                if len(audio) > 1:
                    self.next = 'r_audio_album'
                else:
                    self.next = 'r_audio_single'
            else:
                if form.cleaned_data['content_type'] == 'SINGLE':
                    self.next = 'r_audio_single'
                elif form.cleaned_data['content_type'] == 'ALBUM':
                    self.next = 'r_audio_album'
                else:
                    self.next = 'r_video'
            return HttpResponseRedirect(reverse(self.next))
        else:
            main_info = MainInfo.objects.filter(user_id = user.id)

            if main_info:
                main_info_dict = model_to_dict(*main_info)
                photo = main_info_dict['photo']
                cover = main_info_dict['cover']
                if main_info_dict['cover_psd']:
                    cover_psd = Path(main_info_dict['cover_psd'].name).name
                else:
                    cover_psd = ''
            else:
                photo = ''
                cover = ''
                cover_psd = ''

            return render(request, self.template_name, {'form': form, 
                                                        'form_title': self.form_title,
                                                        'photo': photo, 
                                                        'cover': cover, 
                                                        'cover_psd': cover_psd})


class AudioSingleView(LoginRequiredMixin, FormView):
    template_name = 'release/audio_single.html'
    form_class = AudioSingleForm
    form_title = 'Аудио'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        audio = Audio.objects.filter(user_id = user.id)
        if audio:
            audio_dict = model_to_dict(*audio)

            if audio_dict['audio']:
                song_url = Path(audio_dict['audio'].name).name
            if audio_dict['clean_link']:
                clean_link_url = Path(audio_dict['clean_link'].name).name
            if audio_dict['instrumental']:
                instrumental_url = Path(audio_dict['instrumental'].name).name
            if audio_dict['song_text']:
                song_text_url = Path(audio_dict['song_text'].name).name

            form = self.form_class(initial = audio_dict)
        else:
            song_url = None
            clean_link_url = None
            instrumental_url = None
            song_text_url = None
            form = self.form_class(initial = {'user': user})

        return render(request, self.template_name, {
            'form': form, 
            'form_title': self.form_title,
            'delete_audio': 'delete_audio',
            'delete_clean_link': 'delete_clean_link',
            'delete_instrumental': 'delete_instrumental',
            'delete_song_text': 'delete_song_text',
            'song_url': song_url,
            'clean_link_url': clean_link_url,
            'instrumental_url': instrumental_url,
            'song_text_url': song_text_url})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        add_video = self.request.POST.get('add_video')
        audio = Audio.objects.filter(user_id = user.id)
        if form.is_valid():
            if audio:
                audio_dict = model_to_dict(*audio)
                song = audio_dict['audio']
                clean = audio_dict['clean_link']
                instrumental = audio_dict['instrumental']
                text = audio_dict['song_text'] 
                audio.delete()
                forma = form.save(commit = False)
                if request.FILES.get('audio') == None and audio:
                    forma.audio = song
                if request.FILES.get('clean_link') == None and clean:
                    forma.clean_link = clean
                if request.FILES.get('instrumental') == None and instrumental:
                    forma.instrumental = instrumental
                if request.FILES.get('song_text') == None and text:
                    forma.song_text = text
                forma.save()
            else:
                form.save()

            if add_video == 'NO':
                release_to_cloud(user)
                return HttpResponseRedirect(reverse('r_success'))
            else:
                return HttpResponseRedirect(reverse('r_video'))
        
        else:
            if audio:
                audio_dict = model_to_dict(*audio)
                if audio_dict['audio']:
                    song_url = Path(audio_dict['audio'].name).name
                if audio_dict['clean_link']:
                    clean_link_url = Path(audio_dict['clean_link'].name).name
                if audio_dict['instrumental']:
                    instrumental_url = Path(audio_dict['instrumental'].name).name
                if audio_dict['song_text']:
                    song_text_url = Path(audio_dict['song_text'].name).name
            else:
                song_url = None
                clean_link_url = None
                instrumental_url = None
                song_text_url = None

                
            return render(request, self.template_name, {
            'form': form, 
            'form_title': self.form_title,
            'delete_audio': 'delete_audio',
            'delete_clean_link': 'delete_clean_link',
            'delete_instrumental': 'delete_instrumental',
            'delete_song_text': 'delete_song_text',
            'song_url': song_url,
            'clean_link_url': clean_link_url,
            'instrumental_url': instrumental_url,
            'song_text_url': song_text_url})




class AudioAlbumView(LoginRequiredMixin, FormView):
    template_name = 'release/audio_album.html'
    form_class = AudioAlbumForm
    form_title = 'Аудио'
    fields_for_button = ['songers', 'song_title', 'album_title', 'feat', 'genre', 'fio_songer', 'words_author', 'music_author', 'owner_citizenship', 'record_country', 'timing', 'song_preview', 'lexis', 'audio_link', 'release_year']
    fields = ['songers', 'song_title', 'album_title', 'feat', 'genre', 'fio_songer', 'words_author', 'music_author', 'owner_citizenship', 'record_country', 'timing', 'song_preview', 'lexis', 'audio_link', 'audio', 'clean_link', 'instrumental', 'song_text', 'release_year']

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        num_songs = MainInfo.objects.get(user_id = user.id).num_songs
        audio_formset = formset_factory(self.form_class)
        data = {
            'form-TOTAL_FORMS': str(num_songs),
            'form-INITIAL_FORMS': str(num_songs),
        }
        audio = Audio.objects.filter(user_id = user.id)
        audio_tuple_dict = tuple(model_to_dict(item) for item in audio)

        audio_urls = tuple()
        for item in audio_tuple_dict:
            audio_urls = (*audio_urls, Path(item['audio'].name).name)

        clean_link_urls = tuple()
        for item in audio_tuple_dict:
            clean_link_urls = (*clean_link_urls, Path(item['clean_link'].name).name)

        instrumental_urls = tuple()
        for item in audio_tuple_dict:
            instrumental_urls = (*instrumental_urls, Path(item['instrumental'].name).name)

        song_text_urls = tuple()
        for item in audio_tuple_dict:
            song_text_urls = (*song_text_urls, Path(item['song_text'].name).name)

        if audio:
            for song in range(len(audio)):
                for field in self.fields:
                    data['form-' + str(song) + '-' + field] = getattr(audio[song], field)
            for song in range(num_songs):
                data['form-' + str(song) + '-user'] = user
        else:
            lk = Lk.objects.filter(user_id = user.id)
            if lk:
                fio = lk[0].fio
            else:
                fio = ''
            for num in range(num_songs):
                data['form-' + str(num) + '-fio_songer'] = fio
                data['form-' + str(num) + '-user'] = user.id
        formset = audio_formset(data)
        return render(request, self.template_name, {'button': self.fields_for_button, 
                                                    'formset': formset, 
                                                    'audio_urls': audio_urls, 
                                                    'clean_link_urls': clean_link_urls, 
                                                    'instrumental_urls': instrumental_urls, 
                                                    'song_text_urls': song_text_urls,
                                                    'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        audio_formset = formset_factory(self.form_class)
        formset = audio_formset(data = self.request.POST, files = self.request.FILES)
        add_video = self.request.POST.get('add_video')
        audio = Audio.objects.filter(user_id = user.id)
        if formset.is_valid():

            if audio:
                songs = tuple()
                clean_links = tuple()
                instrumentals = tuple()
                song_texts = tuple()

                for song in audio:
                    songs = (*songs, song.audio)
                    clean_links = (*clean_links, song.clean_link)
                    instrumentals = (*instrumentals, song.instrumental)
                    song_texts = (*song_texts, song.song_text)
                    song.delete()

                for form in range(len(formset)):
                    forma = formset[form].save(commit = False)

                    if form < len(audio):
                        if not forma.audio:
                            forma.audio = songs[form]
                        if not forma.clean_link:
                            forma.clean_link = clean_links[form]
                        if not forma.instrumental:
                            forma.instrumental = instrumentals[form]
                        if not forma.song_text:
                            forma.song_text = song_texts[form]

                    forma.save()
            else:
                for form in formset:
                    form.save()

            if add_video == 'NO':
                release_to_cloud(user)
                return HttpResponseRedirect(reverse('r_success'))
            else:
                return HttpResponseRedirect(reverse('r_video'))
        else:
            audio_tuple_dict = tuple(model_to_dict(item) for item in audio)

            audio_urls = tuple()
            for item in audio_tuple_dict:
                if item['audio']:
                    audio_urls = (*audio_urls, Path(item['audio'].name).name)

            clean_link_urls = tuple()
            for item in audio_tuple_dict:
                if item['clean_link']:
                    clean_link_urls = (*clean_link_urls, Path(item['clean_link'].name).name)

            instrumental_urls = tuple()
            for item in audio_tuple_dict:
                if item['instrumental']:
                    instrumental_urls = (*instrumental_urls, Path(item['instrumental'].name).name)

            song_text_urls = tuple()
            for item in audio_tuple_dict:
                if item['song_text']:
                    song_text_urls = (*song_text_urls, Path(item['song_text'].name).name)

            return render(request, self.template_name, {'button': self.fields_for_button, 
                                                        'formset': formset, 
                                                        'audio_urls': audio_urls, 
                                                        'clean_link_urls': clean_link_urls, 
                                                        'instrumental_urls': instrumental_urls, 
                                                        'song_text_urls': song_text_urls,
                                                        'form_title': self.form_title})


class VideoView(LoginRequiredMixin, FormView):
    template_name = 'release/video.html'
    form_class = VideoForm
    form_title = 'Видеоклип'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        video = Video.objects.filter(user_id = user.id)

        if video:
            video_dict = model_to_dict(video)
            preview = video_dict['video_preview']
            form = self.form_class(initial = video_dict)
        else:
            preview = ''
            form = self.form_class(initial = {'user': user})

        return render(request, self.template_name, {'form': form, 
                                                    'form_title': self.form_title, 
                                                    'delete_preview': 'delete_preview', 
                                                    'preview':preview})

    @silk_profile(name='Video View Post')
    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)

        if form.is_valid():
            video = Video.objects.filter(user_id = user.id)

            if video:
                video_dict = model_to_dict(*video)
                preview = video_dict['video_preview']
                video.delete()
                forma = form.save(commit = False)
                if request.FILES.get('video_preview') == None:
                    forma.video_preview = preview
                forma.save()
            else:
                form.save()

            release_to_cloud(user)
            return HttpResponseRedirect(reverse('r_success'))
        else:
            video = Video.objects.filter(user_id = user.id)

            if video:
                video_dict = model_to_dict(*video)
                preview = video_dict['video_preview']
            else:
                preview = ''

            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'delete_preview': 'delete_preview', 'preview':preview})



def delete_photo(request):
    user = User.objects.get(username = request.user)
    MainInfo.objects.filter(user_id = user.id).update(photo = '')
    return HttpResponseRedirect(reverse('release'))

def delete_cover(request):
    user = User.objects.get(username = request.user)
    MainInfo.objects.filter(user_id = user.id).update(cover = '')
    return HttpResponseRedirect(reverse('release'))

def delete_cover_psd(request):
    user = User.objects.get(username = request.user)
    MainInfo.objects.filter(user_id = user.id).update(cover_psd = '')
    return HttpResponseRedirect(reverse('release'))

def delete_preview(request):
    user = User.objects.get(username = request.user)
    Video.objects.filter(user_id = user.id).update(video_preview = '')
    return HttpResponseRedirect(reverse('r_video'))

def delete_audio(request):
    user = User.objects.get(username = request.user)
    Audio.objects.filter(user_id = user.id).update(audio = '')
    return HttpResponseRedirect(reverse('r_audio_single'))

def delete_clean_link(request):
    user = User.objects.get(username = request.user)
    Audio.objects.filter(user_id = user.id).update(clean_link = '')
    return HttpResponseRedirect(reverse('r_audio_single'))

def delete_instrumental(request):
    user = User.objects.get(username = request.user)
    Audio.objects.filter(user_id = user.id).update(instrumental = '')
    return HttpResponseRedirect(reverse('r_audio_single'))

def delete_song_text(request):
    user = User.objects.get(username = request.user)
    Audio.objects.filter(user_id = user.id).update(song_text = '')
    return HttpResponseRedirect(reverse('r_audio_single'))

def clear_table(request):
    user = User.objects.get(username = request.user)
    audio = Audio.objects.filter(user_id = user.id)
    for song in audio:
        song.delete()
    return HttpResponseRedirect(reverse('r_audio'))

def success_page(request):
    return render(request, 'success.html')

