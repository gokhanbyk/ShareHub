from django.shortcuts import render
from blog.models import *
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    posts = BlogPost.objects.filter(is_active=True)
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

def forum_page_view(request):
    all_posts = BlogPost.objects.filter(is_active=True)
    tags = Tag.objects.filter(is_active=True) 
    categories = Category.objects.filter(is_active=True) 

    paginator = Paginator(all_posts, 5)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = dict(
        tags = tags,
        categories = categories,
        posts = posts
    )
    return render(request, 'page/forum_post.html', context)