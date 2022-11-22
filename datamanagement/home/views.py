from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.models import Users


# Create your views here.
def check_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    if Users.objects.filter(username=username, password=password).exists():
        return HttpResponseRedirect(reverse('users:index'))
    else:
        return HttpResponse('Wrong')