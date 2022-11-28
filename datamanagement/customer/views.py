from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from .models import CustomersOrg, CustomersPer, DocumentOrg, DocumentPer


def index(request):
    customers_p = CustomersPer.objects.all().values()
    customers_o = CustomersOrg.objects.all().values()
    template = loader.get_template('customerIndex.html')
    context = {
        'customer_p': customers_p,
        'customer_o': customers_o,
    }
    return HttpResponse(template.render(context, request))


def add_cp(request):
    template = loader.get_template('customerAddPersonal.html')
    return HttpResponse(template.render({}, request))


def add_co(request):
    template = loader.get_template('customerAddOrg.html')
    return HttpResponse(template.render({}, request))


def add_customerO(request):
    name = request.POST['name']
    taxpayer_num = request.POST['taxpayer_num']
    registered_capital = request.POST['registered_capital']
    email = request.POST['email']
    tel = request.POST['tel']
    address = request.POST['address']
    if CustomersOrg.objects.filter(taxpayer_num=taxpayer_num).exists():
        messages.warning(request, 'Already have this Customer please change!')
        return HttpResponseRedirect(reverse('customer:add_co'))
    elif name == '' or taxpayer_num == '' or registered_capital == '' or email == '' or tel == '' or address == '':
        messages.warning(request, 'Please fill in all form!')
        return HttpResponseRedirect(reverse('customer:add_co'))
    else:
        customer_o = CustomersOrg(name=name, taxpayer_num=taxpayer_num, registered_capital=registered_capital,
                                  email=email, tel=tel, address=address)
        customer_o.save()
    return HttpResponseRedirect(reverse('customer:index'))


def add_customerP(request):
    firstname = request.POST.get('firstname')
    surname = request.POST.get('surname')
    nickname = request.POST.get('nickname')
    email = request.POST.get('email')
    tel = request.POST.get('tel')
    address = request.POST.get('address')
    if CustomersPer.objects.filter(firstname=firstname).exists():
        messages.warning(request, 'Already have this Customer please change!')
        return HttpResponseRedirect(reverse('customer:add_cp'))
    elif firstname == '' or surname == '' or nickname == '' or email == '' or tel == '' or address == '':
        messages.warning(request, 'Please fill in all form!')
        return HttpResponseRedirect(reverse('customer:add_cp'))
    else:
        customer_p = CustomersPer(firstname=firstname, surname=surname, nickname=nickname,
                                  email=email, tel=tel, address=address)
        customer_p.save()
    return HttpResponseRedirect(reverse('customer:index'))
