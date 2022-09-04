from django.contrib import admin
from .models import CustomUser, Profile, Video, Movie

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(Movie)