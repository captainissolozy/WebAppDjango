# Generated by Django 4.1.3 on 2022-12-11 07:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_rename_name_suppliersper_firstname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentorg',
            name='SuppliersOrg',
        ),
        migrations.RemoveField(
            model_name='documentper',
            name='SuppliersPer',
        ),
        migrations.AddField(
            model_name='documentorg',
            name='owner',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documentper',
            name='owner',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
