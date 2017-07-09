
from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),
    url(r'^catalog$', views.catalog, name='catalog'),
    url(r'^spec$', views.spec, name='spec'),
    url(r'^catalog/(?P<alias>[^/]+)', views.get_item, name='items'),
    url(r'^catalog/(?P<alias>[^/]+)', views.get_categories, name='categories_details'),

    #url(r'^1/', views.index, name='index'),
   # url(r'^2/', template_two, name ='template_two'),
    #url(r'^3/', template_three, name ='template_three'),

]