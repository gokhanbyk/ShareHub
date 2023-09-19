from django.shortcuts import render
from blog.models import *

# Create your views here.

def home_view(request):
    posts = BlogPost.objects.filter(is_active=True) # .order_by('-created_at')
    top_posts = posts.order_by('-view_count')[:6]
    tags = Tag.objects.filter(is_active=True) 
    categories = Category.objects.filter(is_active=True) 
    context = dict(
        posts = posts,
        top_posts = top_posts,
        tags = tags,
        categories = categories
    )
    return render(request, 'page/home_page.html', context)