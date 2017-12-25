# -*- coding: utf-8 -*-



from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):

    list_display = 'id', 'text',
    list_editable = 'text',
CommentAdmin = admin.register(Comment)(CommentAdmin)
