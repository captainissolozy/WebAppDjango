from django.db import models


# Create your models here.
class CustomersPer(models.Model):
    firstname = models.CharField(max_length=255)
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


class DocumentOrg(models.Model):
    CustomersOrg = models.ForeignKey(CustomersOrg, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)


class DocumentPer(models.Model):
    owner = models.CharField(max_length=255)
    doc_name = models.CharField(max_length=255)
    path = models.ImageField(upload_to='images_cus/')
