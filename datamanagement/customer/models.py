from django.db import models


# Create your models here.
class CustomersPer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class CustomersOrg(models.Model):
    name = models.CharField(max_length=255)
    taxpayer_num = models.CharField(max_length=255)
    registered_capital = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Document(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_id = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
