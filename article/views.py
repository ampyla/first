# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render ,get_object_or_404
from django.http.response import HttpResponse,Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category , Item, Special, About,Slider
from django.core.exceptions import ObjectDoesNotExist
from form import *
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db.models import Q
import json
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
# Create your views here.




def index(request):
    categories = Category.objects.all().prefetch_related('item_set')
    sliders = Slider.objects.all()

    #get =get_object_or_404(Category,alias='aVTOMATIKA')
    context = {
        'sliders': sliders,
        'categories': categories,
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

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message_mail = form.cleaned_data['message_mail']
            send_mail(subject, message_mail, 'e-egoza@mail.ru', [sender], fail_silently=False)
            messages.success(request, 'Спасибо')
            return HttpResponseRedirect(reverse('contact'))

            #return render(request,'article/contacts.html')
    else:
        form =ContactForm(auto_id=False)

    return render(request, 'article/contacts.html', {'form':form})




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

    return render(request,'article/spec-details.html', context)




def about(request):
    abouts= About.objects.get(alias='abouts')
    context = {
        'abouts' : abouts,
    }
    return render(request, 'article/about.html', context)




def catalog(request):
    categories = Category.objects.all().prefetch_related('item_set')

    context = {
        'categories': categories
    }

    return render(request, 'article/catalog.html', context)

def contactform(request,event ='event',passs='pass'):
    # 2 arguments It is necessary for a stub, since the URL requires 2 more arguments.
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
        except MultiValueDictKeyError:
            name =False
            email=False

        #reception = ['e-egoza@mail.ru']

        send_mail(name,'Here is the.', 'e-egoza@mail.ru',[email], fail_silently=False)
        data = {}
        data['stat'] = "ok";
        return  HttpResponse(json.dumps(data))

    else:
        return HttpResponse(json.dump({"stat" : "notwork"}))


