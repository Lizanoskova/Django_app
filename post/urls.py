
from django.conf.urls import url
from .views import *

from django.contrib.auth.decorators import login_required


urlpatterns = [

    url(r'^(?P<pk>\d+)/$', Post_page.as_view(), name="currentpost"),
    url(r'^(?P<pk>\d+)/comments/$', Post_comments.as_view(), name="postcomments"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(EditPost.as_view()), name="editpost"),
    url(r'^posts/(?P<pk>\d+)/like/$', login_required(PostLikeView.as_view()), name="postlikes"),

]

