from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def get_api(request):
    rdata = requests.get('https://covid19.th-stat.com/api/open/timeline')
    data = rdata.json()
    total = [num for num in range(len(data['Data']))]
    num = str(len(total)-1)
    if request.POST:
        num = request.POST.get('date')
        print(num)

    context = {'datas': zip(reversed(total),
        reversed(data['Data'])), 'current': data['Data'][int(num)]}

    return render(request, 'timeline/timeline.html', context)

