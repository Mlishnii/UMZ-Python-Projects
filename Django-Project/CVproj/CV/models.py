from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Phone = models.CharField(max_length=255)
    summery = models.TextField(max_length=10000)
    skills = models.TextField(max_length=10000)
    experience = models.TextField(max_length=10000)
    education = models.TextField(max_length=10000)
    
