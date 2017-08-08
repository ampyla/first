from django.shortcuts import render ,get_object_or_404
from django.http.response import HttpResponse,Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category , Item, Special
from django.core.exceptions import ObjectDoesNotExist
from form import *
from django.core.mail import send_mail
from django.db.models import Q
# Create your views here.




def index(request):
    categories = Category.objects.all().prefetch_related('item_set')

    #get =get_object_or_404(Category,alias='aVTOMATIKA')
    context = {
        'categories': categories
    }
    return render_to_response('article/index.html', context)




def get_item(request,alias):
    item = get_object_or_404(Item, alias=alias)
    context = {
        'item': item,
    }

    return render(request,'article/card-product.html', context)




def get_categories(request,alias):
    categories = get_object_or_404(Category, alias=alias)
    details_categories = Item.objects.filter(category=categories)


    return render(request,'article/card-categories.html',{'details_categories':details_categories})




def contact(request):

   return render_to_response('article/contacts.html')




def spec(request):
    #list= Item.objects.all().prefetch_related('special_set')
    tov_list = Special.objects.all()
    context ={
        'tov_list': tov_list,
    }
    return render(request,'article/spec-full.html',context)




def spec_details(request,alias):
    tov_list = Special.objects.all()

    try:
        categories_spec = Category.objects.get(alias=alias )
        details_category_spec = Special.objects.filter(category=categories_spec)

    except Category.DoesNotExist:
        try:
            categories_spec = Item.objects.get(alias=alias)
            details_category_spec = Special.objects.filter(item=categories_spec)
        #details_category_spec = Special.objects.filter(Q(category=categories_spec) or Q(item=item_spec))
        except ObjectDoesNotExist:
            raise Http404

    context = {
        'details_category_spec': details_category_spec,
        'tov_list': tov_list,
    }

    return  render(request,'article/spec-details.html', context)




def about(request):
    return render_to_response('article/about.html')




def catalog(request):
    categories = Category.objects.all().prefetch_related('item_set')

    context = {
        'categories': categories
    }

    return render(request, 'article/catalog.html', context)

def contactform(request):
    if request.method=='POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data('subject')
            sender =form.cleaned_data('sender')
            #message = form.cleaned_data('message')
            #copy = form.cleaned_data('copy')

            reception = ['e-egoza@mail.ru']
            try:
                send_mail(subject,)
            except:
                return HttpResponse('Nooooooooo')

            return HttpResponseRedirect('article/thanks')
    else:
        form =  ContactForm()
        return render (request,'article/index.html',{'form':form})



