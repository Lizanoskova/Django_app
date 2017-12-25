# -*- coding: utf-8 -*-


from django.db import models
from django.conf import settings


class Category(models.Model):

    title = models.CharField(max_length=255)
    def __unicode__(self):
        return self.title

# Create your models here.
