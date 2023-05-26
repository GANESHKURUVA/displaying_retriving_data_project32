from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_topics(request):
    if request.method=='POST':
        topics=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topics)[0]
        TO.save()
    return render(request,'insert_topics.html')



def insert_webpage(request):
    TLO=Topic.objects.all()
    d={'topics':TLO}
    if request.method=='POST':
        topics=request.POST['topics']
        name=request.POST['name']
        url=request.POST['url']
        TO=Topic.objects.get(topic_name=topics)
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
     
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    WOL=Webpage.objects.all()
    d={'name':WOL}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        WO=Webpage.objects.get(name=name)

        AO=Accessrecords.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()

    return render(request,'insert_access.html',d)



def retrive_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topics')
        webquery=Webpage.objects.none()

        for i in td:
            webquery=webquery|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webquery}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrive_webpage.html',d)



def checkbox(request):
    LTO=Topic.objects.all()
    d2={'topics':LTO}
    return render(request,'checkbox.html',d2)


def radiobuttons(request):
    LTO=Topic.objects.all()
    d3={'topics':LTO}
    return render(request,'radiobuttons.html',d3)


def update_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    TO=Topic.objects.get_or_create(topic_name='mani')[0]
    TO.save
    Webpage.objects.update_or_create(name='mani',defaults={'topic_name':TO,'url':'http://mani.com'})
    d1={'webpages':Webpage.objects.all()}
    return render(request,'display_webpage.html',d1)
    