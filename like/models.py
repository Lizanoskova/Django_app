# -*- coding: utf-8 -*-



from django.conf import settings
from django.db import models


class Like(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('post.Post', related_name='likes')


# Create your models here.
