# -*- coding: utf-8 -*-



from django.db import models
from django.conf import settings


# Create your models here.
class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField(default='')
    post = models.ForeignKey('post.Post',related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.text
