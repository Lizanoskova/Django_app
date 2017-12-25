
from django.conf.urls import url
from .views import *


urlpatterns = [

    url(r'^$', Category_list.as_view(), name="category_list"),
    url(r'^(?P<pk>\d+)/$', Category_page, name="current_category"),

]
