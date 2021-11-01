import re
from django.shortcuts import render

from google_sheets import Sheet

def calc(request):
    if request.method == 'GET':
        return render(request, 'calc/calc.html')
    else:
        apple_music = request.POST['apple_music']
        spotify = request.POST['spotify']
        vk_boom = request.POST['vk_boom']
        youtube = request.POST['youtube']
        print(type(apple_music))
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
        return render(request, 'calc/calc.html', {'result': result, 'youtube': youtube, 'apple_music': apple_music, 'vk_boom': vk_boom, 'spotify': spotify})