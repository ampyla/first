
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^1/', views.index, name='index'),
   # url(r'^2/', template_two, name ='template_two'),
    #url(r'^3/', template_three, name ='template_three'),

]