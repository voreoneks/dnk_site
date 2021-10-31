from django.shortcuts import render

def calc(request):
    if request.method == 'GET':
        return render(request, 'calc/calc.html')
    else:
        print(request.POST)
        return render(request, 'calc/calc.html')