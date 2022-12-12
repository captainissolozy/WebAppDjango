from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.contrib import messages

from .forms import SupplierForm
from .models import SuppliersOrg, SuppliersPer, DocumentOrg, DocumentPer


def index(request):
    supplier_p = SuppliersPer.objects.all().values()
    supplier_o = SuppliersOrg.objects.all().values()
    doc_org = DocumentOrg.objects.all().values()
    doc_per = DocumentPer.objects.all().values()
    template = loader.get_template('supplierIndex.html')
    context = {
        'supplier_p': supplier_p,
        'supplier_o': supplier_o,
        'doc_org': doc_org,
        'doc_per': doc_per
    }
    return HttpResponse(template.render(context, request))


def inside_org(request, name):
    supplier_o = SuppliersOrg.objects.get(name=name)
    doc_per = []
    if DocumentPer.objects.filter(owner=name).exists():
        doc_per = DocumentPer.objects.filter(owner=name)
    template = loader.get_template('supplierInside.html')
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = supplier_o.name
            form.save()
            doc_per = DocumentPer.objects.filter(owner=name)
    else:
        form = SupplierForm()
    context = {
        'supplier_o': supplier_o,
        'doc_per': doc_per,
        'form': form,
    }
    return HttpResponse(template.render(context, request))



def inside_per(request, email):
    supplier_p = SuppliersPer.objects.get(email=email)
    doc_per = []
    if DocumentPer.objects.filter(owner=email).exists():
        doc_per = DocumentPer.objects.filter(owner=email)
    template = loader.get_template('supplierInsidePer.html')
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = supplier_p.email
            form.save()
            doc_per = DocumentPer.objects.filter(owner=email)
    else:
        form = SupplierForm()
    context = {
        'supplier_p': supplier_p,
        'doc_per': doc_per,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def add_dp(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = SupplierForm()
    return render(request, "test.html", {'form': form})


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
