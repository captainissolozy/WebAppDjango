from django.db import models


# Create your models here.
class SuppliersPer(models.Model):
    firstname = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class SuppliersOrg(models.Model):
    name = models.CharField(max_length=255)
    taxpayer_num = models.CharField(max_length=255)
    registered_capital = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class DocumentOrg(models.Model):
    SuppliersOrg = models.ForeignKey(SuppliersOrg, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)


class DocumentPer(models.Model):
    SuppliersPer = models.ForeignKey(SuppliersPer, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
