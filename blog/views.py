# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#import markdown
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import accident
from blog.models import terms

# from blog.forms import commentForm

class index_view(ListView):
	template_name = "index.html"
	context_object_name = "text"

	def get_queryset(self):
		now = datetime.datetime.now()
		text={'hello':'Hello world!','name':'J','nowtime':now}
		return(text)


class get_accident_list(LoginRequiredMixin,ListView):
	model = accident
	template_name = "accident_list.html"
	content_object_name =  "accident_list"

		#return context

class get_terms_list(LoginRequiredMixin,ListView):
	model = terms
	template_name = "terms_list.html"
	content_object_name =  "terms_list"

class get_terms_detail(LoginRequiredMixin,DetailView):
	template_name = "term.html"
	model = terms
	context_object_name = "term"
	pk_url_kwarg = 'terms_id'
