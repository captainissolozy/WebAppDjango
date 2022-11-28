from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from .models import SuppliersOrg, SuppliersPer, DocumentOrg, DocumentPer
