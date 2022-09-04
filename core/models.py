from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES=(
    ('Adult','Adult'),
    ('Kids','Kids')
)

MOVIE_CHOICES=(
    ('Single Movie','Single'),
    ('Seasonal Movie','Seasonal')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile')

class Profile(models.Model):
    name=models.CharField(max_length=200)
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name + " ===> "+self.age_limit

 
class Movie(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=200, choices=MOVIE_CHOICES)
    videos=models.ManyToManyField('Video')
    flyers=models.ImageField(upload_to='flyers')
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)

    def __str__(self):
       return self.title +" ===> "+self.type + " ===> "+(self.age_limit)

class Video(models.Model):
    title=models.CharField(max_length=200, blank=True,null=True)
    file=models.FileField(upload_to='movies')

    def __str__(self):
        return self.title

