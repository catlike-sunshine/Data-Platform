# -*- coding: utf-8 -*-
#from django.conf.urls import url
from django.conf.urls  import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = "blog"
urlpatterns = [
    url(r'^$', views.index_view.as_view(), name="index"),
<<<<<<< HEAD
=======
    url(r'^accident_list/',views.get_accident_list.as_view(), name="accident_list"),
    url(r'^terms_list/',views.get_terms_list.as_view(), name="trems_list"),
    url(r'^terms/(?P<terms_id>\d+)$', views.get_terms_detail.as_view(), name="terms_detail")
>>>>>>> b62a42baaa96e7f09ee92cbe27dc5d71a0eda923
]
