from django.contrib import admin
from django.db import models

from .models import BlogCategory, BlogPost

# Register your models here.


admin.site.register(BlogCategory)
admin.site.register(BlogPost)

