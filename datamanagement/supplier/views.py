from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from .models import SuppliersOrg, SuppliersPer, DocumentOrg, DocumentPer


def index(request):
    supplier_p = SuppliersPer.objects.all().values()
    supplier_o = SuppliersOrg.objects.all().values()
    template = loader.get_template('supplierIndex.html')
    context = {
        'supplier_p': supplier_p,
        'supplier_o': supplier_o,
    }
    return HttpResponse(template.render(context, request))


def add_sp(request):
    template = loader.get_template('supplierAddPersonal.html')
    return HttpResponse(template.render({}, request))


def add_so(request):
    template = loader.get_template('supplierAddOrg.html')
    return HttpResponse(template.render({}, request))


def add_supplierO(request):
    name = request.POST['name']
    taxpayer_num = request.POST['taxpayer_num']
    registered_capital = request.POST['registered_capital']
    email = request.POST['email']
    tel = request.POST['tel']
    address = request.POST['address']
    if SuppliersOrg.objects.filter(taxpayer_num=taxpayer_num).exists():
        messages.warning(request, 'Already have this Supplier please change!')
        return HttpResponseRedirect(reverse('supplier:add_so'))
    elif name == '' or taxpayer_num == '' or registered_capital == '' or email == '' or tel == '' or address == '':
        messages.warning(request, 'Please fill in all form!')
        return HttpResponseRedirect(reverse('supplier:add_so'))
    else:
        supplier_o = SuppliersOrg(name=name, taxpayer_num=taxpayer_num, registered_capital=registered_capital,
                                  email=email, tel=tel, address=address)
        supplier_o.save()
    return HttpResponseRedirect(reverse('supplier:index'))


def add_supplierP(request):
    firstname = request.POST.get('firstname')
    surname = request.POST.get('surname')
    nickname = request.POST.get('nickname')
    email = request.POST.get('email')
    tel = request.POST.get('tel')
    address = request.POST.get('address')
    if SuppliersPer.objects.filter(firstname=firstname).exists():
        messages.warning(request, 'Already have this Supplier please change!')
        return HttpResponseRedirect(reverse('supplier:add_sp'))
    elif firstname == '' or surname == '' or nickname == '' or email == '' or tel == '' or address == '':
        messages.warning(request, 'Please fill in all form!')
        return HttpResponseRedirect(reverse('supplier:add_sp'))
    else:
        supplier_p = SuppliersPer(firstname=firstname, surname=surname, nickname=nickname,
                                  email=email, tel=tel, address=address)
        supplier_p.save()
    return HttpResponseRedirect(reverse('supplier:index'))
