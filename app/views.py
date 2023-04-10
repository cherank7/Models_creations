from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    tn=input('enter a topic nm:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Topic data inserted successfully')


def insert_web(request):
    tn=input('enter a name:')
    n=input('enter a name:')
    u=input('enter a url:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('WEb data inserted successfully')


def insert_access(request):
    tn=input('enter a name:')
    n=input('enter a name:')
    u=input('enter a url:')
    a=input('enter a author nm:')
    d=input('enter a date:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    ao=Accessrecord.objects.get_or_create(name=wo,author=a,date=d)[0]
    ao.save()
    return HttpResponse('accessrecord data inserted successfully') 


    

