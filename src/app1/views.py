import csv
import datetime
import os.path

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from app1.forms import UserForm


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
        return HttpResponse(f'{word[::2]}')


def login(request):
    if request.method == "POST":
        pass
    else:
        name2 = request.GET.get('name1')
        return redirect('success', name10=name2)


def success(request, name10):
    return HttpResponse(f'hello {name10}')


def add_user(request):
    if not os.path.exists('users.csv'):
        with open('users.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'lastname', 'age'])
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        with open('users.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, lastname, age])
        return HttpResponse(f'name - {name}, lastname - {lastname}, age - {age}')
    else:
        template = loader.get_template('form.html')
        response = template.render({}, request)
        return HttpResponse(response)


def add_user_v2(request):
    if request.method == "POST":
        form = UserForm(request.Post)
        if form.is_valid():
            data = form.cleaned_data

            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            age = request.POST.get('age')
            # content = {'fn': name, 'ln': lastname, 'age': age}
            content = {'user': {'fn': name, 'ln': lastname, 'age': age}}
            return render(request, 'django_06_display.html', content)
        else:
            errors = form.errors
            return HttpResponse(f'error - {errors}')
    else:
        return render(request, 'django_06_form.html', {'form':UserForm()})
