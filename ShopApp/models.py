from django.db import models

# Create your models here.
class ShopDB(models.Model):
    Cat_Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Cat_Image = models.ImageField(upload_to="Profile", null=True, blank=True)

class ProDB(models.Model):
    Cat_Name = models.CharField(max_length=100, null=True, blank=True)
    Pro_Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Pro_Image = models.ImageField(upload_to="Profile", null=True, blank=True)