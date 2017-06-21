from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from .models import Category
#from article.models import Article
# Create your views here.

def index(request):
    tovars =Category.objects.all()
    context = {
	    'tovars': tovars,
	}
    return render_to_response('article/index.html', context)



def contact(request):
   return render_to_response('article/contacts.html')

def spec(request):
   return render_to_response('article/spec.html')

def about(request):
    return render_to_response('article/about.html')

def catalog(request):
    return render_to_response('article/catalog.html')


