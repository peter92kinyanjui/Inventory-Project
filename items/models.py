from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import render


# Create your models here.
class Asset(models.Model):
    asset_name = models.CharField(max_length=100)
    unit_cost = models.IntegerField()
    inv_value = models.IntegerField()
    asset_specs = models.TextField()
    department = models.CharField(max_length=50)
    # asset_img = models.ImageField(upload_to='Product/')
    asset_qty = models.IntegerField()


class Request(models.Model):
    staff_no= models.CharField(max_length=50)
    staff_fname = models.CharField(max_length=100)
    staff_sname = models.CharField(max_length=100)
    asset_name = models.CharField(max_length=100)
    asset_specs = models.TextField()
    department = models.CharField(max_length=50)
    asset_qty = models.IntegerField()
    allocation_status = models.CharField(max_length=100)

# class User(models.Model):
#     staff_no= models.CharField(max_length=50)
#     staff_fname = models.CharField(max_length=100)
#     staff_sname = models.CharField(max_length=100)
#     staff_email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)






