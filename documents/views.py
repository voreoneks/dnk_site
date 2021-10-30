from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.expressions import F
from django.forms import formset_factory
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView
from datetime import datetime
from google_sheets import Sheet
from django.forms.models import model_to_dict

from .forms import *
from .models import *

def docs_to_sheet(user):
    date_time = str(datetime.now())
    docs_sheet = Sheet('Документы!A3:DC3')

    main_info_docs = MainInfoDocs.objects.get(user_id = user.id)
    main_info_docs_dict = model_to_dict(main_info_docs)
    docs_values = tuple()
    main_info_docs_values = (
        date_time, main_info_docs_dict['you_are'], main_info_docs_dict['partners_value'], main_info_docs_dict['artist_fio'], main_info_docs_dict['artist_name'], main_info_docs_dict['phone_number'], main_info_docs_dict['email'], main_info_docs_dict['socials'], main_info_docs_dict['release_type']
    )
    docs_values += main_info_docs_values

    try:
        orginfoiprf = OrgInfoIprf.objects.get(user_id = user.id)
        orginfoiprf_dict = model_to_dict(orginfoiprf)
        orginfoiprf_values = (
            orginfoiprf_dict['fio'], orginfoiprf_dict['ogrnip'], orginfoiprf_dict['inn'], orginfoiprf_dict['bank'], orginfoiprf_dict['r_s'], orginfoiprf_dict['bik'], orginfoiprf_dict['inn_bank'], orginfoiprf_dict['k_s']
        )
    except:
        orginfoiprf_values = tuple('' for i in range(8))

    docs_values += orginfoiprf_values

    try:
        orginfoipin = OrgInfoIpin.objects.get(user_id = user.id)
        orginfoipin_dict = model_to_dict(orginfoipin)
        orginfoipin_values = (
            orginfoipin_dict['fio'], orginfoipin_dict['citizen'], orginfoipin_dict['id_number'], orginfoipin_dict['bank'], orginfoipin_dict['r_s'], orginfoipin_dict['bik'], orginfoipin_dict['inn_bank'], orginfoipin_dict['k_s']
        )
    except:
        orginfoipin_values = tuple('' for i in range(8))

    docs_values += orginfoipin_values

    try:
        orginfosam = OrgInfoSam.objects.get(user_id = user.id)
        orginfosam_dict = model_to_dict(orginfosam)
        orginfosam_values = (
            orginfosam_dict['fio'], str(orginfosam_dict['birthday']), orginfosam_dict['series_num'], orginfosam_dict['who_issued'], str(orginfosam_dict['when_issued']), orginfosam_dict['code_pod'], orginfosam_dict['birth_place'], orginfosam_dict['reg'], orginfosam_dict['bank'], orginfosam_dict['r_s'], orginfosam_dict['bik'], orginfosam_dict['inn_bank'], orginfosam_dict['k_s'], orginfosam_dict['inn'], orginfosam_dict['snils'], ''
        )
    except:
        orginfosam_values = tuple('' for i in range(16))

    docs_values += orginfosam_values

    try:
        orginfoooo = OrgInfoOoo.objects.get(user_id = user.id)
        orginfoooo_dict = model_to_dict(orginfoooo)
        orginfoooo_values = (
            orginfoooo_dict['name'], orginfoooo_dict['fio_gen_dir'], orginfoooo_dict['ogrn'], orginfoooo_dict['inn'], orginfoooo_dict['kpp'], orginfoooo_dict['yur_address'], orginfoooo_dict['fact_address'], orginfoooo_dict['bank'], orginfoooo_dict['r_s'], orginfoooo_dict['bik'], orginfoooo_dict['inn_bank'], orginfoooo_dict['k_s']
        )
    except:
        orginfoooo_values = tuple('' for i in range(12))

    docs_values += orginfoooo_values

        

    try:
        audio_docs = AudioDocs.objects.filter(user_id = user.id)
        audio_docs_tuple_dict = tuple(model_to_dict(item) for item in audio_docs)
        audio_docs_values = (
            audio_docs_tuple_dict[0]['songers'], audio_docs_tuple_dict[0]['album_title'], audio_docs_tuple_dict[0]['song_title'], audio_docs_tuple_dict[0]['words_author'], audio_docs_tuple_dict[0]['music_author'], audio_docs_tuple_dict[0]['phon_maker'], audio_docs_tuple_dict[0]['timing'], '', audio_docs_tuple_dict[0]['release_year']
        )
    except:
        audio_docs = []
        audio_docs_values = tuple('' for i in range(9))
    
    docs_values += audio_docs_values

    try:
        video_docs = VideoDocs.objects.get(user_id = user.id)
        video_docs_dict = model_to_dict(video_docs)
        video_docs_values = (
            video_docs_dict['songers'], video_docs_dict['video_title'], video_docs_dict['words_author'], video_docs_dict['music_author'], video_docs_dict['phon_maker'], video_docs_dict['director'], video_docs_dict['timing'], video_docs_dict['release_year'], video_docs_dict['production_country']
        )
    except:
        video_docs_values = tuple('' for i in range(9))

    docs_values += video_docs_values

    licence = Licence.objects.get(user_id = user.id)
    licence_dict = model_to_dict(licence)
    licence_values = (
        licence_dict['music_author'], licence_dict['words_author'], licence_dict['phon_maker']
    )
    docs_values += licence_values


    music_author = MusicAuthor.objects.filter(user_id = user.id)
    music_author_tuple_dict = tuple(model_to_dict(item) for item in music_author)
    music_author_values = (
        music_author_tuple_dict[0]['fio'], str(music_author_tuple_dict[0]['birthday']), music_author_tuple_dict[0]['citizen'], music_author_tuple_dict[0]['passport'], music_author_tuple_dict[0]['birth_place'], music_author_tuple_dict[0]['reg'], music_author_tuple_dict[0]['author_email'], music_author_tuple_dict[0]['fin_conditions']
    )

    docs_values += music_author_values

    words_author = WordsAuthor.objects.filter(user_id = user.id)
    words_author_tuple_dict = tuple(model_to_dict(item) for item in words_author)
    words_author_values = (
        words_author_tuple_dict[0]['fio'], str(words_author_tuple_dict[0]['birthday']), words_author_tuple_dict[0]['citizen'], words_author_tuple_dict[0]['passport'], words_author_tuple_dict[0]['birth_place'], words_author_tuple_dict[0]['reg'], words_author_tuple_dict[0]['author_email'], words_author_tuple_dict[0]['fin_conditions']
    )

    docs_values += words_author_values

    try:
        others = Others.objects.filter(user_id = user.id)
        others_tuple_dict = tuple(model_to_dict(item) for item in others)
        others_values = (
            others_tuple_dict[0]['creative_name'], others_tuple_dict[0]['songs'], others_tuple_dict[0]['fio'], str(others_tuple_dict[0]['birthday']), others_tuple_dict[0]['citizen'], others_tuple_dict[0]['passport'], others_tuple_dict[0]['birth_place'], others_tuple_dict[0]['reg'], others_tuple_dict[0]['fin_conditions']
        )
    except:
        others = []
        others_values = tuple('' for i in range(9))

    docs_values += others_values

    try:
        phon_maker = PhonMaker.objects.filter(user_id = user.id)
        phon_maker_tuple_dict = tuple(model_to_dict(item) for item in phon_maker)
        phon_maker_values = (
            phon_maker_tuple_dict[0]['fio'], str(phon_maker_tuple_dict[0]['birthday']), phon_maker_tuple_dict[0]['citizen'], phon_maker_tuple_dict[0]['passport'], phon_maker_tuple_dict[0]['birth_place'], phon_maker_tuple_dict[0]['reg'], phon_maker_tuple_dict[0]['author_email'], phon_maker_tuple_dict[0]['fin_conditions']
        )
    except:
        phon_maker = []
        phon_maker_values = tuple('' for i in range(8))

    docs_values += phon_maker_values

    print(docs_values)

    docs_data = {
        'range': 'Документы!A3:DC3',
        'majorDimension': 'ROWS',
        'values': [docs_values,]
    }

    docs_sheet.append(docs_data)


    add_rows = Sheet('Документы!A3:DC3')
    max_len = max(len(audio_docs), len(music_author), len(words_author), len(others), len(phon_maker))

    for i in range(1, max_len):
        add_rows_values = tuple('' for i in range(53))
        try:
            add_audio_docs_value = (
                audio_docs_tuple_dict[i]['songers'], audio_docs_tuple_dict[i]['album_title'], audio_docs_tuple_dict[i]['song_title'], audio_docs_tuple_dict[i]['words_author'], audio_docs_tuple_dict[i]['music_author'], audio_docs_tuple_dict[i]['phon_maker'], audio_docs_tuple_dict[i]['timing'], '', audio_docs_tuple_dict[i]['release_year']
            )
        except:
            add_audio_docs_value = tuple('' for i in range(9))
        add_rows_values += add_audio_docs_value

        try:
            add_music_author_values = (
                music_author_tuple_dict[i]['fio'], str(music_author_tuple_dict[i]['birthday']), music_author_tuple_dict[i]['citizen'], music_author_tuple_dict[i]['passport'], music_author_tuple_dict[i]['birth_place'], music_author_tuple_dict[i]['reg'], music_author_tuple_dict[i]['author_email'], music_author_tuple_dict[i]['fin_conditions']
            )
        except:
            add_music_author_values = tuple('' for i in range(8))
        add_rows_values += add_music_author_values

        try:
            add_words_author_values = (
                words_author_tuple_dict[i]['fio'], str(words_author_tuple_dict[i]['birthday']), words_author_tuple_dict[i]['citizen'], words_author_tuple_dict[i]['passport'], words_author_tuple_dict[i]['birth_place'], words_author_tuple_dict[i]['reg'], words_author_tuple_dict[i]['author_email'], words_author_tuple_dict[i]['fin_conditions']
            )
        except:
            add_words_author_values = tuple('' for i in range(8))
        add_rows_values += add_words_author_values

        try:
            add_others_values = (
                others_tuple_dict[i]['creative_name'], others_tuple_dict[i]['songs'], others_tuple_dict[i]['fio'], str(others_tuple_dict[i]['birthday']), others_tuple_dict[i]['citizen'], others_tuple_dict[i]['passport'], others_tuple_dict[i]['birth_place'], others_tuple_dict[i]['reg'], others_tuple_dict[i]['author_email'], others_tuple_dict[i]['fin_conditions']
            )
        except:
            add_others_values = tuple('' for i in range(9))
        add_rows_values += add_others_values

        try:
            add_phon_maker_values = (
                phon_maker_tuple_dict[i]['fio'], str(phon_maker_tuple_dict[i]['birthday']), phon_maker_tuple_dict[i]['citizen'], phon_maker_tuple_dict[i]['passport'], phon_maker_tuple_dict[i]['birth_place'], phon_maker_tuple_dict[i]['reg'], phon_maker_tuple_dict[i]['author_email'], phon_maker_tuple_dict[i]['fin_conditions']
            )
        except:
            add_phon_maker_values = tuple('' for i in range(8))
        add_rows_values += add_phon_maker_values

        add_rows_data = {
            'range': 'Документы!A3:DC3',
            'majorDimension': 'ROWS',
            'values': [add_rows_values, ]
        }

        add_rows.append(add_rows_data)


    spaces = Sheet('Документы!A3:DC3')
    spaces_values = tuple('.' for i in range(107))
    spaces_data = {
        'range': 'Документы!A3:DC3',
        'majorDimension': 'ROWS',
        'values': [spaces_values,]
    }
    spaces.append(spaces_data)


    main_info_docs.delete()

    try:
        OrgInfoIprf.objects.get(user_id = user.id).delete()
    except:
        pass

    try:
        OrgInfoIpin.objects.get(user_id = user.id).delete()
    except:
        pass

    try:
       OrgInfoSam.objects.get(user_id = user.id).delete()
    except:
        pass

    try:
        OrgInfoOoo.objects.get(user_id = user.id).delete()
    except:
        pass

    try:
        audio_docs = AudioDocs.objects.filter(user_id = user.id)
        for item in audio_docs:
            item.delete()
    except:
        pass

    try:
        VideoDocs.objects.get(user_id = user.id).delete()
    except:
        pass

    licence.delete()

    for item in music_author:
        item.delete()

    for item in words_author:
        item.delete()

    try:
        others = Others.objects.filter(user_id = user.id)
        for item in others:
            item.delete()
    except:
        pass

    try:
        phon_maker = PhonMaker.objects.filter(user_id = user.id)
        for item in phon_maker:
            item.delete()
    except:
        pass






class MainInfoDocsView(LoginRequiredMixin, FormView):
    template_name = 'documents/documents.html'
    form_class = MainInfoDocsForm
    form_title = 'Для лицензиара'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        try:
            object_ = MainInfoDocs.objects.get(user_id = user.id)
            object_dict = model_to_dict(object_)
            cover = object_dict['cover']
            form = self.form_class(initial = object_dict)
            delete_link = 'delete_cover'
        except:
            delete_link = ''
            cover = ''
            form = self.form_class(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'cover': cover, 'delete_link': delete_link})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            try:
                object_ = MainInfoDocs.objects.get(user_id = user.id)
                cover = object_.cover
                object_.delete()
                if cover:
                    forma = form.save(commit = False)
                    forma.cover = cover
                forma.save()
            except:
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
        try:
            object_ = self.get_model().objects.get(user_id = user.id)
            object_dict = model_to_dict(object_)
            skan_passport = object_dict['skan_passport']
            delete_skan_passport = 'delete_skan_passport'
            form = self.get_form_class()(initial = object_dict)
        except:
            skan_passport = ''
            delete_skan_passport = ''
            form = self.get_form_class()(initial = {'user': user})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'skan_passport': skan_passport, 'delete_skan_passport': delete_skan_passport})

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            objects = self.get_model().objects.filter(user_id = user.id)
            if len(objects) != 0:
                for item in objects:
                    item.delete()
            form.save() 
            main_info_docs = MainInfoDocs.objects.get(user_id = user.id)
            release_type = main_info_docs.release_type
            if release_type == 'SINGLE' or release_type == 'ALBUM':
                return HttpResponseRedirect(reverse('d_audio'))
            else:
                return HttpResponseRedirect(reverse('d_video'))                
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})


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
            return HttpResponseRedirect(reverse('music_author', args=[1]))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})


class MusicAuthorView(LoginRequiredMixin, FormView):
    template_name = 'documents/music_author.html'
    form_class = MusicAuthorForm
    form_description = ''

    def get(self, request, *args, **kwargs):
        num_author = kwargs['num_author']
        self.form_title = 'Автор музыки ' + str(num_author)
        user = User.objects.get(username = request.user)
        objects = MusicAuthor.objects.filter(user_id = user.id)
        if num_author > len(objects) + 1:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        if num_author <= len(objects):
            form = self.form_class(initial = model_to_dict(objects.get(number = num_author)))
        else:
            form = self.form_class(initial = {'user': user, 'number': num_author})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'num_author': num_author})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        num_author = kwargs['num_author']
        objects = MusicAuthor.objects.filter(user_id = user.id)
        self.form_title = 'Автор музыки ' + str(num_author)
        form = self.form_class(data = request.POST, files = request.FILES)
        if form.is_valid():
            if num_author <= len(objects):
                objects.get(number = num_author).delete()
            form.save()
            one_more = request.POST.get('one_more')
            if num_author < len(objects):
                return HttpResponseRedirect(reverse('music_author', args=[num_author + 1]))
            else:
                if one_more == 'ONE_MORE_YES':
                    if num_author >= 5:
                        self.form_description = 'Нельзя создать больше пяти авторов музыки.' 
                        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description, 'num_author': num_author})
                    else:
                        return HttpResponseRedirect(reverse('music_author', args=[num_author + 1]))
                else:
                    return HttpResponseRedirect(reverse('words_author', args=[1]))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})


class WordsAuthorView(LoginRequiredMixin, FormView):
    template_name = 'documents/words_author.html'
    form_class = WordsAuthorForm
    form_description = ''

    def get(self, request, *args, **kwargs):
        num_author = kwargs['num_author']
        self.form_title = 'Автор слов ' + str(num_author)
        user = User.objects.get(username = request.user)
        objects = WordsAuthor.objects.filter(user_id = user.id)
        if num_author <= len(objects):
            form = self.form_class(initial = model_to_dict(objects.get(number = num_author)))
        else:
            form = self.form_class(initial = {'user': user, 'number': num_author})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'num_author': num_author})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        num_author = kwargs['num_author']
        objects = WordsAuthor.objects.filter(user_id = user.id)
        self.form_title = 'Автор слов ' + str(num_author)
        form = self.form_class(data = request.POST, files = request.FILES)
        if form.is_valid():
            if num_author <= len(objects):
                objects.get(number = num_author).delete()
            form.save()
            one_more = request.POST.get('one_more')
            if num_author < len(objects):
                return HttpResponseRedirect(reverse('words_author', args=[num_author + 1]))
            else:
                if one_more == 'ONE_MORE_YES':
                    if num_author >= 5:
                        self.form_description = 'Нельзя создать больше пяти авторов слов.' 
                        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description, 'num_author': num_author})
                    else:
                        return HttpResponseRedirect(reverse('words_author', args=[num_author + 1]))
                else:
                    return HttpResponseRedirect(reverse('others', args=[1]))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})


class OthersView(LoginRequiredMixin, FormView):
    template_name = 'documents/others.html'
    form_class = OthersForm
    form_description = ''

    def get(self, request, *args, **kwargs):
        num_others = kwargs['num_others']
        self.form_title = 'Соисполнитель ' + str(num_others)
        user = User.objects.get(username = request.user)
        objects = Others.objects.filter(user_id = user.id)
        if num_others <= len(objects):
            form = self.form_class(initial = model_to_dict(objects.get(number = num_others)))
        else:
            form = self.form_class(initial = {'user': user, 'number': num_others})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'num_others': num_others})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        num_others = kwargs['num_others']
        objects = Others.objects.filter(user_id = user.id)
        self.form_title = 'Соисполнитель ' + str(num_others)
        form = self.form_class(data = request.POST, files = request.FILES)
        if form.is_valid():
            if num_others <= len(objects):
                objects.get(number = num_others).delete()
            form.save()
            one_more = request.POST.get('one_more')
            if num_others < len(objects):
                return HttpResponseRedirect(reverse('others', args=[num_others + 1]))
            else:
                if one_more == 'ONE_MORE_YES':
                    if num_others >= 5:
                        self.form_description = 'Нельзя создать больше пяти соисполнителей.' 
                        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description, 'num_others': num_others})
                    else:
                        return HttpResponseRedirect(reverse('others', args=[num_others + 1]))
                else:
                    return HttpResponseRedirect(reverse('phon_maker', args=[1]))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})


class PhonMakerView(LoginRequiredMixin, FormView):
    template_name = 'documents/phon_maker.html'
    form_description = '<p>Пожалуйста, укажите данные изготовителя фонограммы.</p> <p>Изготовитель фонограммы - тот, кто взял на себя осуществление сведения с творческой составляющей, то есть тот, кто продумал финальное звучание трека (это может быть сам артист, продюсер и тд)</p>'
    form_class = PhonMakerForm

    def get(self, request, *args, **kwargs):
        num_phon_maker = kwargs['num_phon_maker']
        self.form_title = 'Изготовитель фонограммы ' + str(num_phon_maker)
        user = User.objects.get(username = request.user)
        objects = PhonMaker.objects.filter(user_id = user.id)
        if num_phon_maker <= len(objects):
            form = self.form_class(initial = model_to_dict(objects.get(number = num_phon_maker)))
        else:
            form = self.form_class(initial = {'user': user, 'number': num_phon_maker})
        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'num_phon_maker': num_phon_maker})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        num_phon_maker = kwargs['num_phon_maker']
        objects = PhonMaker.objects.filter(user_id = user.id)
        self.form_title = 'Изготовитель фонограммы ' + str(num_phon_maker)
        form = self.form_class(data = request.POST, files = request.FILES)
        if form.is_valid():
            if num_phon_maker <= len(objects):
                objects.get(number = num_phon_maker).delete()
            form.save()
            one_more = request.POST.get('one_more')
            if num_phon_maker < len(objects):
                return HttpResponseRedirect(reverse('phon_maker', args=[num_phon_maker + 1]))
            else:
                if one_more == 'ONE_MORE_YES':
                    if num_phon_maker >= 5:
                        self.form_description = 'Нельзя создать больше пяти соисполнителей.' 
                        return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description, 'num_phon_maker': num_phon_maker})
                    else:
                        return HttpResponseRedirect(reverse('phon_maker', args=[num_phon_maker + 1]))
                else:
                    docs_to_sheet(user)
                    return HttpResponseRedirect(reverse('d_success'))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})



def delete_music_author(request, *args, **kwargs):
    num_author = int(request.GET.get('num_author'))
    user = User.objects.get(username = request.user)
    objects = MusicAuthor.objects.filter(user_id = user.id)
    objects[num_author - 1].delete()
    objects = MusicAuthor.objects.filter(user_id = user.id)
    for i in range(len(objects)):
        object_ = objects[i]
        object_.number = i + 1 
        object_.save()
    if num_author > 1:
        link = num_author - 1 
    else:
        link = 1
    return HttpResponseRedirect(reverse('music_author', args=[link]))

def delete_words_author(request, *args, **kwargs):
    num_author = int(request.GET.get('num_author'))
    user = User.objects.get(username = request.user)
    objects = WordsAuthor.objects.filter(user_id = user.id)
    objects[num_author - 1].delete()
    objects = WordsAuthor.objects.filter(user_id = user.id)
    for i in range(len(objects)):
        object_ = objects[i]
        object_.number = i + 1 
        object_.save()
    if num_author > 1:
        link = num_author - 1 
    else:
        link = 1
    return HttpResponseRedirect(reverse('words_author', args=[link]))

def delete_others(request, *args, **kwargs):
    num_others = int(request.GET.get('num_others'))
    user = User.objects.get(username = request.user)
    objects = Others.objects.filter(user_id = user.id)
    objects[num_others - 1].delete()
    objects = Others.objects.filter(user_id = user.id)
    for i in range(len(objects)):
        object_ = objects[i]
        object_.number = i + 1 
        object_.save()
    if num_others > 1:
        link = num_others - 1 
    else:
        link = 1
    return HttpResponseRedirect(reverse('others', args=[link]))

def delete_phon_maker(request, *args, **kwargs):
    num_phon_maker = int(request.GET.get('num_phon_maker'))
    user = User.objects.get(username = request.user)
    objects = PhonMaker.objects.filter(user_id = user.id)
    objects[num_phon_maker - 1].delete()
    objects = PhonMaker.objects.filter(user_id = user.id)
    for i in range(len(objects)):
        object_ = objects[i]
        object_.number = i + 1 
        object_.save()
    if num_phon_maker > 1:
        link = num_phon_maker - 1 
    else:
        link = 1
    return HttpResponseRedirect(reverse('phon_maker', args=[link]))

def delete_cover(request):
    user = User.objects.get(username = request.user)
    object_ = MainInfoDocs.objects.filter(user_id = user.id).update(cover = '')
    return HttpResponseRedirect(reverse('documents'))

def delete_skan_passport(request):
    user = User.objects.get(username = request.user)
    object_ = OrgInfoSam.objects.filter(user_id = user.id).update(skan_passport = '')
    return HttpResponseRedirect(reverse('orginfo'))

def success_page(request):
    return render(request, 'success.html')
