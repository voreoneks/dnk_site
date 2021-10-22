from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView

from .forms import *
from .models import *


def method_get(request, model, form_class, template_name):
    user = User.objects.get(username = request.user)
    objects = model.objects.filter(user_id = user.id).values()
    if len(objects) != 0:
        for item in objects:
            data = item
        data['user'] = user
        form = form_class(initial = data)
    else:
        form = form_class(initial = {'user': user})
    return render(request, template_name, {'form': form})


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
            org_info = self.get_model().objects.filter(user_id = user.id)
            if len(org_info) != 0:
                for item in org_info:
                    item.delete()
            form.save()
            return HttpResponseRedirect(reverse('choice', args=[1]))
        else:
            return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

    

def choice(request, id):
    if request.method == 'GET':
        context = dict()
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
            return HttpResponseRedirect(reverse('audio'))
        elif choice == 'CLIP':
            return HttpResponseRedirect(reverse('video'))
        elif choice == 'MUSIC_CITIZEN':
            return HttpResponseRedirect(reverse('music_author', args=['citizen']))
        elif choice == 'MUSIC_FOREIGN':
            return HttpResponseRedirect(reverse('music_author', args=['foreign']))
        elif choice == 'WORDS_CITIZEN':
            return HttpResponseRedirect(reverse('words_author', args=['citizen']))
        elif choice == 'WORDS_FOREIGN':
            return HttpResponseRedirect(reverse('words_author', args=['foreign']))
        elif choice == 'PHON_MAKER_CITIZEN':
            print(request.POST)
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
            video = VideoDocs.objects.filter(user_id = user.id)
            if len(video) != 0:
                for item in video:
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
            licence = Licence.objects.filter(user_id = user.id)
            if len(licence) != 0:
                for item in licence:
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
                return HttpResponseRedirect(reverse('choice', args=[3]))
            else:
                return render(request, self.template_name, {'form': form, 'form_title': self.form_title})

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
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST, files = request.FILES)
        user = User.objects.get(username = request.user)
        if form.is_valid():
            licence = Others.objects.filter(user_id = user.id)
            if len(licence) != 0:
                for item in licence:
                    item.delete()
            form.save()
            return HttpResponseRedirect(reverse('choice', args=[4]))
        else:
            return render(request, self.template_name, {'form': form})


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
                return HttpResponseRedirect(reverse('success'))
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
                return HttpResponseRedirect(reverse('success'))
            else:
                return render(request, self.template_name, {'form': form, 'form_title': self.form_title, 'form_description': self.form_description})


def success_page(request):
    return render(request, 'success.html')
