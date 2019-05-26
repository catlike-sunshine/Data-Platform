from django.http import HttpResponse
import datetime
from django.shortcuts import render


def index(request):
	now = datetime.datetime.now()
	text={'hello':'Hello world!','name':'J','nowtime':now}
	return render(request,'index.html',text)

def content(request):
	return render(request, 'content.html')
