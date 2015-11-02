from django.shortcuts import render, get_object_or_404
from models import Article, Image, Content, Contributor 
from django.http import HttpResponse

from django.template import RequestContext, loader

from .models import Article, Contributor

# Create your views here.

def all_contrib(request):
    contributors = Contributor.objects.all()

    data = {'contributors': contributors}

    return render(request, 'contrib.html', data)

def index(request):
	latest_article_list = Article.objects.order_by('-pub_date')[:5]
	context = {'latest_article_list': latest_article_list}
	return render(request, 'index.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail.html', {'article': article})

def cont(request, contributor_id):
    contributor = get_object_or_404(Contributor, pk=contributor_id)
    return render(request, 'con.html', {'contributor': contribut})
