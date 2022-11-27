# Create your models here.
from django.db import models


# Create your models here.
class Projects(models.Model):
    proj_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    sales = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class Document(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_id = models.CharField(max_length=255)
    path = models.CharField(max_length=255)


class Quotations(models.Model):
    doc_id = models.CharField(max_length=255)
    q_id = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    exp_date = models.CharField(max_length=255)

