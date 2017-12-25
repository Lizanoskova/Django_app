
from django.conf.urls import url
from core.views import  Main_page

urlpatterns = [
    url(r'^$', Main_page.as_view()),
]

