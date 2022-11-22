from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from .models import Users


def index(request):
    users = Users.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    username = request.POST['username']
    password = request.POST['password']
    role = request.POST['role']
    if Users.objects.filter(username=username).exists() or username == '' or password == '' or role == '':
        messages.warning(request, 'Already have this username please change!')
        return HttpResponseRedirect(reverse('users:add'))
    else:
        users = Users(username=username, password=password, role=role)
        users.save()
    return HttpResponseRedirect(reverse('users:index'))


def delete(request, id):
    users = Users.objects.get(id=id)
    users.delete()
    return HttpResponseRedirect(reverse('users:index'))


def update(request, id):
    users = Users.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    username = request.POST['user']
    password = request.POST['password']
    role = request.POST['role']
    users = Users.objects.get(id=id)
    users.user = username
    users.password = password
    users.role = role
    users.save()
    return HttpResponseRedirect(reverse('users:index'))