from django.shortcuts import render,get_object_or_404
from blogs.models import Post
# Create your views here.
def post_detail(request,id):
    post=get_object_or_404(Post,pk=id)
    post.read=True
    post.views+=1
    post.save()
    
    return render(request, "blogs/post.html",{'post':post})