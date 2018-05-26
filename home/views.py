from django.shortcuts import render,redirect
from blogs.models import Post
from events.models import Event
from django.utils import timezone


# Create your views here.
def get_index(request):
     posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[0:11]
     events = Event.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[0:11]
     return render(request, "home/index.html",{'posts':posts,'events':events})
     
     
def get_contacts(request):
    return render(request, "home/contact.html")
    
    
def get_faq(request):
    return render(request, "home/faq.html")
    
    
def get_news(request):
     posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
     return render(request, "home/news.html",{'posts':posts})
    
    
def get_events(request):
     events = Event.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
     return render(request, "home/events.html",{'events':events})
    