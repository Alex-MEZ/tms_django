from django.shortcuts import render

import datetime

from django.http import HttpResponse
from django.shortcuts import redirect


def get_data(request):
    data = datetime.datetime.now()
    return HttpResponse(data)


def two_pow(request, number):
    result = 2 ** int(number)
    return HttpResponse(f'2 ** {number} = {result}')


def hello_admin(request):
    return HttpResponse(f'hello admin')


def hello_guest(request, name):
    return HttpResponse(f'hello {name}')


def hello_user(request, user):
    if user == 'admin':
        return redirect('admin')
    else:
        return redirect('hello_guest', name=user)

def my_word(request, word):
    if len(word) % 2:
        return redirect('get_time')
    else:
        return HttpResponse (f'{word [::2]}')
