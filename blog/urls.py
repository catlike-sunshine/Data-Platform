# -*- coding: utf-8 -*-
#from django.conf.urls import url
from django.conf.urls  import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = "blog"
urlpatterns = [
    url(r'^$', views.index_view.as_view(), name="index"),
    url(r'^accident_list/',views.get_accident_list.as_view(), name="accident_list")
]
