from django.shortcuts import render
from google_sheets import Sheet


def calc(request):
    form_title = 'Калькулятор авансов'
    form_description = 'Добавьте информацию по прослушиваниям ваших релизов за последние 6 месяцев. <br>Информацию по прослушиваниям вы можете получить от вашего музыкального издательства, агрегатора и в приложениях Apple Music for Artists / Spotify for Artists'
    if request.method == 'GET':
        return render(request, 'calc/calc.html', {'form_title': form_title, 
                                                  'form_description': form_description})
    else:
        apple_music = request.POST['apple_music']
        spotify = request.POST['spotify']
        vk_boom = request.POST['vk_boom']
        youtube = request.POST['youtube']
        if '.' in apple_music or '.' in spotify or '.' in vk_boom or '.' in youtube:
            error = 'Значение должно быть целым числом.'
            return render(request, 'calc/calc.html', {'error': error})
        else:
            error = ''
        count_sheet = Sheet('Sheet1!C7:L21', spreadsheet_id='1-xnfaYFok7QU49YxuRbVk8M7ub5ZfZzzgIwoUYgo5sE', value_input_option='USER_ENTERED', insert_data_option='OVERWRITE')
        count_value = (apple_music, spotify, 0, 0, youtube, vk_boom, 0, 0, 0)
        count_data = {
            'range': 'Sheet1!C7:L21',
            'majorDimension': 'ROWS',
            'values': [count_value,]
        }
        count_sheet.write(count_data)

        artist_income = count_sheet.read('C20:D20', 'ROWS')
        first_cell, second_cell = (artist_income['values'][0])
        first_cell = first_cell.replace(',', '.').replace('\xa0', '')
        second_cell = second_cell.replace(',', '.').replace('\xa0', '')
        result = float(first_cell) + float(second_cell)
        result = round(result, 2)
        return render(request, 'calc/calc.html', {'result': result, 
                                                  'youtube': youtube, 
                                                  'apple_music': apple_music, 
                                                  'vk_boom': vk_boom, 
                                                  'spotify': spotify, 
                                                  'form_title': form_title, 
                                                  'form_description': form_description})
