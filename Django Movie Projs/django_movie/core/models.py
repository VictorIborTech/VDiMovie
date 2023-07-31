from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid
# Create your models here.


class CustomUser(AbstractUser):
    profile = models.ManyToManyField('Profile',blank=True)


AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
    
)
MOVIES_CHOICES = (
    ('Seasonal', 'Seasonal'),
    ('Single', 'Single'),
    ('Comedy', 'Comedy'),
    
    
)

class Profile(models.Model):
    name = models.CharField(max_length=200)
    age_limit = models.CharField(max_length=25, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4) #This Allow us request for a particular model


class Movie(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True) #This add the date and time the movie was created.
    uuid = models.UUIDField(default=uuid.uuid4) 
    movie_type = models.CharField(max_length=50, choices=MOVIES_CHOICES)
    videos = models.ManyToManyField('Video')
    thumbnail = models.ImageField(upload_to='movie_thumbnails')
    age_limit = models.CharField(max_length=25, choices=AGE_CHOICES)
    

class Video(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    file= models.FileField(upload_to='movies')

    
    