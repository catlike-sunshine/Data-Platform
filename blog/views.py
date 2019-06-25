# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#import markdown
import datetime

from blog.models import article
from blog.models import accident
from blog.models import comment
from blog.models import terms

# from blog.forms import commentForm

class index_view(ListView):
	template_name = "index.html"
	context_object_name = "text"

	def get_queryset(self):
		now = datetime.datetime.now()
		text={'hello':'Hello world!','name':'J','nowtime':now}
		return(text)

class get_article_detail(DetailView):
	template_name = "article.html"
	model = article
	context_object_name = "article"
	pk_url_kwarg = 'article_id'

	#def get_object(self, queryset=None):
	#	obj = super(get_article_detail, self).get_object()
	#	obj.content = markdown.markdown(obj.content, extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc',])
	#	return (obj)

class get_article_list(ListView):
	model = article
	template_name = "page.html"
	context_object_name = "article_list"

	#def get_queryset(self):
	#	article_list = article.objects.all()
	#	for obj in article_list:
	#		obj.content = markdown.markdown(obj.content,)
	#	return (article_list)

class get_accident_list(ListView):
	model = accident
	template_name = "accident_list.html"
	content_object_name =  "accident_list"


class get_comments(ListView):
	model = comment
	# 前端使用Ajax请求评论数据，故该模板仅包含评论部分
	template_name = "comment/article_comment.html"
	context_object_name = "comment_list"
	pk_url_kwarg = 'article_id'
	#分页，每页10条评论
	paginate_by = 10
	# 筛选目标文章的评论，article_id为url中的参数
	def get_queryset(self):
		return article.comment.filter()
    #def get_context_data(self, **kwargs):
    #    context = super().get_body_data(**kwargs)
    #    context['form'] = commentForm()

		#if context["page_obj"].number == 1 and self.request.user.is_authenticated:
		# 评论的第一页需要提供表单让用户创建新评论
        #    context['form'] = commentForm({'article': self.kwargs['article_id']})
        #elif context["page_obj"].number == 1：
        #    # 没有登录的用户需要登录，传article_id是为了在评论中创建url，详细的在模板中解释
        #    context['article_id'] = self.kwargs['article_id']

        # 计算评论的次序
        #first_num = context["paginator"].count - \
        #    self.paginate_by * (context["page_obj"].number - 1)
        #last_num = first_num - self.paginate_by
        #context['comment_list'] = zip(range(first_num, last_num, -1), context['comment_list'])

		#return context

class get_terms_list(ListView):
	model = terms
	template_name = "terms_list.html"
	content_object_name =  "terms_list"

class get_terms_detail(DetailView):
	template_name = "term.html"
	model = terms
	context_object_name = "term"
	pk_url_kwarg = 'terms_id'