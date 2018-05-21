from django.shortcuts import render,redirect
from blogs.models import Post
from django.utils import timezone


# Create your views here.
def get_index(request):
     posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[0:11]
     return render(request, "home/index.html",{'posts':posts})
    