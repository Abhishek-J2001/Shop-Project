from django.db import models

# Create your models here.
class ContactDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class RegisterDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)