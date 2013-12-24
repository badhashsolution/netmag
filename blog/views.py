from django.shortcuts import render, get_object_or_404
from blog.models import Post

# WGG 2013-12-24 05:51:20 - add in items to display views
def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published = True)
    # now return the rendered template
    return render(request, 'blog/index.html',{'posts':posts})

def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug = slug)
    # now return the rendered template
    return render(request, 'blog/post.html',{'post':post})

