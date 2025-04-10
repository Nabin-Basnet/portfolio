from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)    #title of th project
    description = models.TextField()                            #description of project
    image = models.ImageField(upload_to='projects/')            #logo or image for project
    live_demo = models.URLField(blank=True, null=True)          #live demo url(button)
    github_link = models.URLField(blank=True, null=True)        #github link
    

class Skill(models.Model):
    name = models.CharField(max_length=100)  # Name of the skill
    description = models.TextField()         # Description of the skill
    icon = models.ImageField(upload_to='skills/icons/', null=True, blank=True) 

class ContactInfo(models.Model):
    name = models.CharField(max_length=100)        # Name of the person
    email = models.EmailField()                     # Email of the person
    phone = models.CharField(max_length=15, null=True, blank=True)      #phone number

class PersonalDetail(models.Model):
    first_name = models.CharField(max_length=100)         # First name of the user
    last_name = models.CharField(max_length=100)          # Last name of the user
    address = models.TextField(null=True, blank=True)      # Address of the user
    photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Profile photo
    description = models.TextField(null=True, blank=True) 