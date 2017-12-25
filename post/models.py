# -*- coding: utf-8 -*-



from django.db import models
from django.conf import settings
from category.models import Category


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255,verbose_name='Title')
    text = models.TextField()
    blog = models.ForeignKey('blog.Blog',related_name='posts')
    categories = models.ManyToManyField(Category,related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title






# Create your models here.
