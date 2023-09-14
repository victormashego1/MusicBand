"""Models are registered here in order to access them in Django Admin.

Import:

from django.contrib import admin\n
from .models import Music, Choice

Models:

admin.site.register(Music)\n
admin.site.register(Choice)


"""
from django.contrib import admin
from .models import Music, Choice

# Register your models here.
admin.site.register(Music)
admin.site.register(Choice)
