from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(Movie)
admin.site.register(Video)