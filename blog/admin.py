from django.contrib import admin
from .models import Post
# Register your models here.

# Make our model visible on the admin page
admin.site.register(Post)