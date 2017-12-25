# -*- coding: utf-8 -*-



from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = 'id', 'title',
    list_editable = 'title',
PostAdmin = admin.register(Post)(PostAdmin)
