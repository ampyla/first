from django.shortcuts import render ,get_object_or_404
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from .models import Category , Item
# Create your views here.

def index(request):
    categories = Category.objects.all().prefetch_related('item_set')

    #get =get_object_or_404(Category,alias='aVTOMATIKA')
    context = {
        'categories': categories
    }
    return render_to_response('article/index.html', context)

def get_category(request,alias):
    category = get_object_or_404(Category, alias=alias)
    tovars = Item.objects.filter(category=category)
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


