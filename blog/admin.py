# -*- coding: utf-8 -*-



from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):

    list_display = 'id', 'title',
    list_editable = 'title',
BlogAdmin = admin.register(Blog)(BlogAdmin)
