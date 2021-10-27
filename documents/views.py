from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView
from datetime import datetime
from google_sheets import Sheet
from django.forms.models import model_to_dict

from .forms import *
from .models import *

# def docs_to_sheet(user):
#     date_time = str(datetime.now())
#     docs_sheet = Sheet('Документы!A3:EU3')
#     main_info_docs = MainInfoDocs.objects.get(user_id = user.id)
#     main_info_docs_dict = model_to_dict(main_info_docs)
#     docs_values = tuple()
#     exist_flags = tuple()
#     main_info_docs_values = (
#         date_time, main_info_docs_dict['you_are'], main_info_docs_dict['partners_value'], main_info_docs_dict['artist_fio'], main_info_docs_dict['artist_name'], main_info_docs_dict['phone_number'], main_info_docs_dict['email'], main_info_docs_dict['socials']
#     )
#     docs_values += main_info_docs_values
#     exist_flags += (1,)

#     try:
#         orginfoiprf = OrgInfoIprf.objects.filter(user_id = user.id)
#         orginfoiprf_dict = model_to_dict(orginfoiprf)
#         orginfoiprf_values = (
#             orginfoiprf_dict['fio'], orginfoiprf_dict['ogrnip'], orginfoiprf_dict['inn'], orginfoiprf_dict['bank'], orginfoiprf_dict['r_s'], orginfoiprf_dict['bik'], orginfoiprf_dict['inn_bank'], orginfoiprf_dict['k_s']
#         )
#         exist_flags += (1,)
#     except:
#         orginfoiprf_values = tuple('' for i in range(8))
#         exist_flags += (0,)

#     docs_values += orginfoiprf_values

#     try:
#         orginfoipin = OrgInfoIpin.objects.filter(user_id = user.id)
#         orginfoipin_dict = model_to_dict(orginfoipin)
#         orginfoipin_values = (
#             orginfoipin_dict['fio'], orginfoipin_dict['citizen'], orginfoipin_dict['id_number'], orginfoipin_dict['bank'], orginfoipin_dict['r_s'], orginfoipin_dict['bik'], orginfoipin_dict['inn_bank'], orginfoipin_dict['k_s']
#         )
#         exist_flags += (1,)
#     except:
#         orginfoipin_values = tuple('' for i in range(8))
#         exist_flags += (0,)

#     docs_values += orginfoipin_values

#     try:
#         orginfosam = OrgInfoSam.objects.filter(user_id = user.id)
#         orginfosam_dict = model_to_dict(orginfosam)
#         orginfosam_values = (
#             orginfosam_dict['fio'], orginfosam_dict['birthday'], orginfosam_dict['series_num'], orginfosam_dict['who_issued'], orginfosam_dict['when_issued'], orginfosam_dict['code_pod'], orginfosam_dict['birth_place'], orginfosam_dict['reg'], orginfosam_dict['bank'], orginfosam_dict['r_s'], orginfosam_dict['bik'], orginfosam_dict['inn_bank'], orginfosam_dict['k_s'], orginfosam_dict['inn'], orginfosam_dict['snils'], ''
#         )
#         exist_flags += (1,)
#     except:
#         orginfosam_values = tuple('' for i in range(16))
#         exist_flags += (0,)

#     docs_values += orginfosam_values

#     try:
#         orginfoooo = OrgInfoOoo.objects.filter(user_id = user.id)
#         orginfoooo_dict = model_to_dict(orginfoooo)
#         orginfoooo_values = (
#             orginfoooo_dict['name'], orginfoooo_dict['fio_gen_dir'], orginfoooo_dict['ogrn'], orginfoooo_dict['inn'], orginfoooo_dict['kpp'], orginfoooo_dict['yur_address'], orginfoooo_dict['fact_address'], orginfoooo_dict['bank'], orginfoooo_dict['r_s'], orginfoooo_dict['bik'], orginfoooo_dict['inn_bank'], orginfoooo_dict['k_s']
#         )
#         exist_flags += (1,)
#     except:
#         orginfoooo_values = tuple('' for i in range(12))
#         exist_flags += (0,)

#     docs_values += orginfoooo_values

        
#     audio_docs = AudioDocs.objects.filter(user_id = user.id)
#     audio_docs_tuple_dict = tuple(model_to_dict(item) for item in audio_docs)

#     try:
#         audio_docs_values = (
#             audio_docs_tuple_dict[0]['songers'], audio_docs_tuple_dict[0]['album_title'], audio_docs_tuple_dict[0]['song_title'], audio_docs_tuple_dict[0]['words_author'], audio_docs_tuple_dict[0]['music_author'], audio_docs_tuple_dict[0]['phon_maker'], audio_docs_tuple_dict[0]['timing'], '', audio_docs_tuple_dict[0]['release_year']
#         )
#         exist_flags += (1,)
#     except:
#         audio_docs_values = tuple('' for i in range(9))
#         exist_flags += (0,)
    
#     docs_values += audio_docs_values

#     try:
#         video_docs = VideoDocs.objects.filter(user_id = user.id)
#         video_docs_dict = model_to_dict(video_docs)
#         video_docs_values = (
#             video_docs_dict['songers'], video_docs_dict['video_title'], video_docs_dict['words_author'], video_docs_dict['music_author'], video_docs_dict['phon_maker'], video_docs_dict['director'], video_docs_dict['timing'], video_docs_dict['release_year'], video_docs_dict['production_country']
#         )
#         exist_flags += (1,)
#     except:
#         video_docs_values = tuple('' for i in range(9))
#         exist_flags += (0,)

#     docs_values += video_docs_values

#     licence = Licence.objects.get(user_id = user.id)
#     licence_dict = model_to_dict(licence)
#     licence_values = (
#         licence_dict['music_author'], licence_dict['words_author'], licence_dict['phon_maker']
#     )
#     docs_values += licence_values
#     exist_flags += (1,)














#     try:
#         add_audio_sheet = Sheet('Релиз!A3:AM3')
#         add_audio_values = []
#         for i in range(1, len(audio_docs_tuple_dict)):
#             add_audio_values.append(tuple(('', '',  '',  '',  '',  '',  '', audio_docs_tuple_dict[i]['songers'], audio_docs_tuple_dict[i]['song_title'], audio_docs_tuple_dict[i]['album_title'], audio_docs_tuple_dict[i]['feat'], audio_docs_tuple_dict[i]['genre'], audio_docs_tuple_dict[i]['fio_songer'], audio_docs_tuple_dict[i]['words_author'], audio_docs_tuple_dict[i]['music_author'], audio_docs_tuple_dict[i]['owner_citizenship'], audio_docs_tuple_dict[i]['record_country'], audio_docs_tuple_dict[i]['timing'], audio_docs_tuple_dict[i]['song_preview'], audio_docs_tuple_dict[i]['lexis'], '', '', audio_docs_tuple_dict[i]['audio_link'], '', audio_docs_tuple_dict[i]['clean_link'], '', audio_docs_tuple_dict[i]['release_year'])))

#         add_audio_data = {
#             'range': 'Релиз!A3:AM3',
#             'majorDimension': 'ROWS',
#             'values': add_audio_values
#             }
#         add_audio_sheet.append(add_audio_data)
#     except:
#         pass

#     spaces = Sheet('Релиз!A3:AM3')
#     spaces_values = [tuple('.' for i in range(39))]
#     spaces_data = {
#         'range': 'Релиз!A3:AM3',
#         'majorDimension': 'ROWS',
#         'values': spaces_values
#     }
#     spaces.append(spaces_data)
#     main_info.delete()
#     for item in audio:
#         item.delete()
#     video.delete()


class MainInfoDocsView(LoginRequiredMixin, FormView):
    template_name = 'documents/documents.html'
    form_class = MainInfoDocsForm
    form_title = 'Для лицензиара'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        objects = MainInfoDocs.objects.filter(user_id = user.id).values()
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
            objects = MainInfoDocs.objects.filter(user_id = user.id)
            if len(objects) != 0:
                for item in objects:
                    item.delete()
            form.save()
            return HttpResponseRedirect('orginfo')
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})
        

class OrgInfoView(LoginRequiredMixin, FormView):
    template_name = 'documents/orginfo.html'

    def get_form_class(self):
        user = User.objects.get(username = self.request.user)
        you_are = MainInfoDocs.objects.filter(user_id = user.id)[0].you_are
        if you_are == 'IPRF':
            self.form_title = 'ИП РФ'
            return OrgInfoIprfForm
        elif you_are == 'IPIN':
            self.form_title = 'ИП Иностранный'
            return OrgInfoIpinForm
        elif you_are == 'SAM':
            self.form_title = 'Самозанятый'
            return OrgInfoSamForm
        else: 
            self.form_title = 'ООО'
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
        user = User.objects.get(username = request.user)
        objects = self.get_model().objects.filter(user_id = user.id).values()
        if len(objects) != 0:
            for item in objects:
                data = item
            data['user'] = user
            form = self.get_form_class()(initial = data)
        else:
            form = self.get_form_class()(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            objects = self.get_model().objects.filter(user_id = user.id)
            if len(objects) != 0:
                for item in objects:
                    item.delete()
            form.save() 
            return HttpResponseRedirect(reverse('choice', args=[1]))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    

def choice(request, id):
    if request.method == 'GET':
        if id == 1:
            form = '<p><input type="radio" name="choice" value="SINGLE" required id="id_content_type_0" checked><label for="id_content_type_0">Сингл</label></p><p><input type="radio" name="choice" value="ALBUM" required id="id_content_type_1"><label for="id_content_type_1">Альбом</label></p><p><input type="radio" name="choice" value="CLIP" required id="id_content_type_2"><label for="id_content_type_2">Видеоклип</label></p>'
            context = {
                'field_title': 'Тип релиза',
                'form': form,
            }
        elif id == 2:
            form = '<p><input type="radio" name="choice" value="MUSIC_CITIZEN" required id="id_music_author_0" checked><label for="id_music_author_0">Гражданин РФ</label></p><p><input type="radio" name="choice" value="MUSIC_FOREIGN" required id="id_music_author_1"><label for="id_music_author_1">Иностранный гражданин</label></p>'
            context = {
                'field_title': 'Автор музыки',
                'form': form,
            }
        elif id == 3:
            form = '<p><input type="radio" name="choice" value="WORDS_CITIZEN" required id="id_music_author_0" checked><label for="id_music_author_0">Гражданин РФ</label></p><p><input type="radio" name="choice" value="WORDS_FOREIGN" required id="id_music_author_1"><label for="id_music_author_1">Иностранный гражданин</label></p></p>'
            context = {
                'field_title': 'Автор текста',
                'form': form,
            }
        elif id == 4:
            form = '<p><input type="radio" name="choice" value="PHON_MAKER_CITIZEN" required id="id_music_author_0" checked><label for="id_music_author_0">Гражданин РФ</label></p><p><input type="radio" name="choice" value="PHON_MAKER_FOREIGN" required id="id_music_author_1"><label for="id_music_author_1">Иностранный гражданин</label></p><p><input type="radio" name="choice" value="PHON_MAKER_SELF" required id="id_music_author_2"><label for="id_music_author_2">Сам артист</label></p></p>'
            context = {
                'field_title': 'Изготовитель фонограммы',
                'form': form,
            }
        return render(request, 'documents/choice.html', context)
    else:
        choice = request.POST.get('choice')
        if choice == 'SINGLE' or choice == 'ALBUM':
            return HttpResponseRedirect(reverse('d_audio'))
        elif choice == 'CLIP':
            return HttpResponseRedirect(reverse('d_video'))
        elif choice == 'MUSIC_CITIZEN':
            return HttpResponseRedirect(reverse('music_author', args=['citizen']))
        elif choice == 'MUSIC_FOREIGN':
            return HttpResponseRedirect(reverse('music_author', args=['foreign']))
        elif choice == 'WORDS_CITIZEN':
            return HttpResponseRedirect(reverse('words_author', args=['citizen']))
        elif choice == 'WORDS_FOREIGN':
            return HttpResponseRedirect(reverse('words_author', args=['foreign']))
        elif choice == 'PHON_MAKER_CITIZEN':
            return HttpResponseRedirect(reverse('phon_maker', args=['citizen']))
        elif choice == 'PHON_MAKER_FOREIGN':
            return HttpResponseRedirect(reverse('phon_maker', args=['foreign']))
        elif choice == 'PHON_MAKER_SELF':
            return HttpResponseRedirect(reverse('success'))


class AudioDocsView(LoginRequiredMixin, FormView):
    template_name = 'documents/audio.html'
    form_class = AudioDocsForm
    form_title = 'Аудио'

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
        return render(request, self.template_name, {'button': self.form_class._meta.fields, 'formset': formset, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        audio_formset = formset_factory(self.form_class)
        formset = audio_formset(data = self.request.POST, files = self.request.FILES)
        add_video = self.request.POST.get('add_video')
        print(formset.errors)
        if formset.is_valid():
            audio = AudioDocs.objects.filter(user_id = user.id)
            if len(audio) != 0:
                for song in audio:
                    song.delete()
            for form in formset:
                form.save()
            if add_video == 'NO':
                return HttpResponseRedirect(reverse('licence'))
            else:
                return HttpResponseRedirect(reverse('d_video'))
        else:
            return render(request, self.template_name, {'button': self.form_class._meta.fields, 'formset': formset, 'form_title': self.form_title})


class VideoDocsView(LoginRequiredMixin, FormView):
    template_name = 'documents/video.html'
    form_class = VideoDocsForm
    form_title = 'Видеоклип'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        objects = VideoDocs.objects.filter(user_id = user.id).values()
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
            objects = VideoDocs.objects.filter(user_id = user.id)
            if len(objects) != 0:
                for item in objects:
                    item.delete()
            form.save()
            return HttpResponseRedirect(reverse('licence'))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})


class LicenceView(LoginRequiredMixin, FormView):
    template_name = 'documents/licence.html'
    form_class = LicenceForm
    form_title = 'Права на материал'
    form_description = '<p>Отчуждение - это когда авторы текста/музыки отчуждают тебе права на текст/музыку, исключительные права передаются в полном объеме без ограничения по способам, сроку и территории использования.<br>Варианты: ты не платишь им роялти за использование текста, платишь фиксированную сумму, платишь процент роялти в период действия договора.</p> <p>Лицензия - авторы текста/музыки передают тебе права на текст на срок действиях нашего договора с тобой (5 лет + пролонгация), предоставляется только право использования определенными способами, на определенной территории и в течение установленного срока, ты платишь им процент роялти за использование, либо выплачиваешь вознаграждение один раз.</p>'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        objects = Licence.objects.filter(user_id = user.id).values()
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
            objects = Licence.objects.filter(user_id = user.id)
            if len(objects) != 0:
                for item in objects:
                    item.delete()
            form.save()
            return HttpResponseRedirect(reverse('choice', args=[2]))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})


class MusicAuthorView(LoginRequiredMixin, FormView):
    template_name = 'documents/music_author.html'

    def get(self, request, *args, **kwargs):
        author = kwargs.get('author')
        if author == 'citizen':
            self.form_title = 'Гражданин РФ'
            user = User.objects.get(username = request.user)
            objects = MusicCitizen.objects.filter(user_id = user.id).values()
            if len(objects) != 0:
                for item in objects:
                    data = item
                data['user'] = user
                form = MusicCitizenForm(initial = data)
            else:
                form = MusicCitizenForm(initial = {'user': user})
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

        elif author == 'foreign':
            self.form_title = 'Иностранный гражданин'
            user = User.objects.get(username = request.user)
            objects = MusicForeign.objects.filter(user_id = user.id).values()
            if len(objects) != 0:
                for item in objects:
                    data = item
                data['user'] = user
                form = MusicForeignForm(initial = data)
            else:
                form = MusicForeignForm(initial = {'user': user})
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        author = kwargs.get('author')
        one_more = request.POST.get('one_more')
        if author == 'citizen':
            self.form_title = 'Гражданин РФ'
            form = MusicCitizenForm(data = request.POST, files = request.FILES)
            user = User.objects.get(username = request.user)
            if form.is_valid():
                objects = MusicCitizen.objects.filter(user_id = user.id)
                if len(objects) != 0:
                    for item in objects:
                        item.delete()
                form.save()
            #     num_last_obj = AudioDocs.objects.order_by('-pk')[0].pk
            #     if one_more == 'YES':
            #         return HttpResponseRedirect(reverse('choice', args=[2]))
            #     else:
            #         return HttpResponseRedirect(reverse('choice', args=[3]))
            # else:
            #     return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

        elif author == 'foreign':
            self.form_title = 'Иностранный гражданин'
            form = MusicForeignForm(data = request.POST, files = request.FILES)
            user = User.objects.get(username = request.user)
            if form.is_valid():
                objects = MusicForeign.objects.filter(user_id = user.id)
                if len(objects) != 0:
                    for item in objects:
                        item.delete()
                form.save()
                return HttpResponseRedirect(reverse('choice', args=[3]))
            else:
                return render(request, self.template_name, {'form': form, 'form_title': self.form_title})


class WordsAuthorView(LoginRequiredMixin, FormView):
    template_name = 'documents/words_author.html'

    def get(self, request, *args, **kwargs):
        author = kwargs.get('author')
        if author == 'citizen':
            self.form_title = 'Гражданин РФ'
            user = User.objects.get(username = request.user)
            objects = WordsCitizen.objects.filter(user_id = user.id).values()
            if len(objects) != 0:
                for item in objects:
                    data = item
                data['user'] = user
                form = WordsCitizenForm(initial = data)
            else:
                form = WordsCitizenForm(initial = {'user': user})
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

        elif author == 'foreign':
            self.form_title = 'Иностранный гражданин'
            user = User.objects.get(username = request.user)
            objects = WordsForeign.objects.filter(user_id = user.id).values()
            if len(objects) != 0:
                for item in objects:
                    data = item
                data['user'] = user
                form = WordsForeignForm(initial = data)
            else:
                form = WordsForeignForm(initial = {'user': user})
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    def post(self, request, *args, **kwargs):
        one_more = request.POST.get('one_more')
        author = kwargs.get('author')
        if author == 'citizen':
            self.form_title = 'Гражданин РФ'
            form = WordsCitizenForm(data = request.POST, files = request.FILES)
            user = User.objects.get(username = request.user)
            if form.is_valid():
                objects = WordsCitizen.objects.filter(user_id = user.id)
                if len(objects) != 0:
                    for item in objects:
                        item.delete()
                form.save()
                return HttpResponseRedirect(reverse('others'))
            else:
                return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

        elif author == 'foreign':
            self.form_title = 'Иностранный гражданин'
            form = WordsForeignForm(data = request.POST, files = request.FILES)
            user = User.objects.get(username = request.user)
            if form.is_valid():
                objects = WordsForeign.objects.filter(user_id = user.id)
                if len(objects) != 0:
                    for item in objects:
                        item.delete()
                form.save()
                return HttpResponseRedirect(reverse('others'))
            else:
                return render(request, self.template_name, {'form': form, 'form_title': self.form_title})


class OthersView(LoginRequiredMixin, FormView):
    template_name = 'documents/others.html'
    form_class = OthersForm
    form_title = 'Другие исполнители'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        objects = Others.objects.filter(user_id = user.id).values()
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
            objects = Others.objects.filter(user_id = user.id)
            if len(objects) != 0:
                for item in objects:
                    item.delete()
            form.save()
            return HttpResponseRedirect(reverse('choice', args=[4]))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})


class PhonMakerView(LoginRequiredMixin, FormView):
    template_name = 'documents/phon_maker.html'
    form_description = '<p>Пожалуйста, укажите данные изготовителя фонограммы.</p> <p>Изготовитель фонограммы - тот, кто взял на себя осуществление сведения с творческой составляющей, то есть тот, кто продумал финальное звучание трека (это может быть сам артист, продюсер и тд)</p>'

    def get(self, request, *args, **kwargs):
        maker = kwargs.get('maker')
        if maker == 'citizen':
            self.form_title = 'Гражданин РФ'
            user = User.objects.get(username = request.user)
            objects = PhonMakerCitizen.objects.filter(user_id = user.id).values()
            if len(objects) != 0:
                for item in objects:
                    data = item
                data['user'] = user
                form = PhonMakerCitizenForm(initial = data)
            else:
                form = PhonMakerCitizenForm(initial = {'user': user})
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})

        elif maker == 'foreign':
            self.form_title = 'Иностранный гражданин'
            user = User.objects.get(username = request.user)
            objects = PhonMakerForeign.objects.filter(user_id = user.id).values()
            if len(objects) != 0:
                for item in objects:
                    data = item
                data['user'] = user
                form = PhonMakerForeignForm(initial = data)
            else:
                form = PhonMakerForeignForm(initial = {'user': user})
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})

    def post(self, request, *args, **kwargs):
        one_more = request.POST.get('one_more')
        maker = kwargs.get('maker')
        if maker == 'citizen':
            self.form_title = 'Гражданин РФ'
            form = PhonMakerCitizenForm(data = request.POST, files = request.FILES)
            user = User.objects.get(username = request.user)
            if form.is_valid():
                objects = PhonMakerCitizen.objects.filter(user_id = user.id)
                if len(objects) != 0:
                    for item in objects:
                        item.delete()
                form.save()
                return HttpResponseRedirect(reverse('d_success'))
            else:
                return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})

        elif maker == 'foreign':
            self.form_title = 'Иностранный гражданин'
            form = PhonMakerForeignForm(data = request.POST, files = request.FILES)
            user = User.objects.get(username = request.user)
            if form.is_valid():
                objects = PhonMakerForeign.objects.filter(user_id = user.id)
                if len(objects) != 0:
                    for item in objects:
                        item.delete()
                form.save()
                return HttpResponseRedirect(reverse('d_success'))
            else:
                return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})


def success_page(request):
    return render(request, 'success.html')
