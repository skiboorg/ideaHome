from django.contrib import admin
from .models import *


class BlogPostAdmin(admin.ModelAdmin):

    exclude = ['name_slug']

    class Meta:
        model = BlogPost


admin.site.register(BlogPost,BlogPostAdmin)
