from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from .forms import *
from .models import *
import json


# Create your views here.

login_required(login_url='user:login_view')
def fav_update(request):
    if request.method == 'POST':
        post = get_object_or_404(BlogPost, slug = request.POST.get('slug'))
        if post:
            post_fav, created = UserPostFav.objects.get_or_create(
                user = request.user,
                post = post,
            )
            if not created:
                post_fav.is_deleted =  not post_fav.is_deleted
                post_fav.save()

    
    return JsonResponse({'status': 200})



login_required(login_url='user:login_view')
def create_blog_post_view(request):
    title = 'Yeni Blog Post: '
    form = BlogPostModelForm()
   
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            tags_json = form.cleaned_data.get('tag')
            tags = json.loads(tags_json)
            for item in tags:
                value = item["value"]
                tag_item, created = Tag.objects.get_or_create(title=value.lower())
                tag_item.is_active = True
                tag_item.save()
                post.tag.add(tag_item)
            messages.success(request, 'Blog postunuz basariyla kaydedildi..')
            return redirect('home_view')

    context = dict(
        form = form,
        title = title,
    )
    return render(request, 'comon_components/form.html', context)


def tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug = tag_slug)
    posts = BlogPost.objects.filter(tag = tag)
    if request.user.is_authenticated:
        ids = request.user.userpostfav_set.filter(is_deleted=False).values_list('post_id', flat=True)
        favs=BlogPost.objects.filter(id__in=ids, is_active=True)

        context = dict(
        tag = tag,
        favs = favs
        )
        return render(request, 'blog/post_list.html', context)

        
    context = dict(
        tag = tag,
    )

    return render(request, 'blog/post_list.html', context)


def category_view(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    posts = BlogPost.objects.filter(category = category)
    if request.user.is_authenticated:
        ids = request.user.userpostfav_set.filter(is_deleted=False).values_list('post_id', flat=True)
        favs=BlogPost.objects.filter(id__in=ids, is_active=True)

        context = dict(
        category = category,
        favs = favs
        )
        return render(request, 'blog/post_list.html', context)

    context = dict(
        category = category,
    )

    return render(request, 'blog/post_list.html', context)

def search_view(request):
    if 'q' in request.GET and request.GET.get('q'):

        if request.user.is_authenticated:
            ids = request.user.userpostfav_set.filter(is_deleted=False).values_list('post_id', flat=True)
            favs=BlogPost.objects.filter(id__in=ids, is_active=True)

            q = request.GET.get('q')
        
            categories = Category.objects.filter(title__contains = q)    
            tags = Tag.objects.filter(title__contains = q)    
            posts = BlogPost.objects.filter(title__contains = q) or BlogPost.objects.filter(category__in = categories) or BlogPost.objects.filter(tag__in = tags)
            
            return render(request, 'blog/search.html', {
                        'q':q,
                        'posts':posts,
                        'favs':favs
            })
        

        q = request.GET.get('q')
        
        categories = Category.objects.filter(title__contains = q)    
        tags = Tag.objects.filter(title__contains = q)    
        posts = BlogPost.objects.filter(title__contains = q) or BlogPost.objects.filter(category__in = categories) or BlogPost.objects.filter(tag__in = tags)
        
        return render(request, 'blog/search.html', {
            'q':q,
            'posts':posts,
        })
        


    return render(request, 'blog/search.html', {})


login_required(login_url='user:login_view')
def post_edit_view(request, post_slug):
    
    post = get_object_or_404(BlogPost, slug = post_slug)

    if not post.user == request.user:
        messages.warning(request, 'Bu Post Bilgisini Düzenleyemezsiniz!')
        return redirect('home_view')
    

    title = post.title
    form = BlogPostModelForm(instance=post)

    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(title=item.get('value').lower())
                tag_item.is_active = True
                tag_item.save()
                f.tag.add(tag_item)
            messages.success(request, 'Blog Postunuz Basariyla Duzenlendi..')
            return redirect('home_view')

    context = dict(
        title = title,
        form = form
    )

    return render(request, 'comon_components/form.html', context)
