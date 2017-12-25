
from django.conf.urls import url
from blog.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^$', Blog_list.as_view(), name="blogview"),
    url(r'^(?P<pk>\d+)/$', Blog_page.as_view(), name="currentblog"),
   # url(r'^(?P<pk>\d+)/new/$',login_required(New_Post.as_view()), name="post_creation"),

]
