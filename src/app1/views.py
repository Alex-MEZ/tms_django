from django.shortcuts import render

import datetime

from django.http import HttpResponse

def get_data(request):
    data = datetime.datetime.now()
    return HttpResponse(data)
