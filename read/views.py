from django.shortcuts import render,get_object_or_404, redirect
from blog.models import *
from user.models import *
from blog.forms import CommentForm

# Create your views here.


def all_posts_view(request, user_slug):
    profile = get_object_or_404(Profile, slug = user_slug)
    ids = request.user.userpostfav_set.filter(is_deleted=False).values_list('post_id', flat=True)
    favs=BlogPost.objects.filter(id__in=ids, is_active=True)
    context = dict(
        profile = profile,
        posts = BlogPost.objects.filter(user = profile.user, is_active=True),
        favs = favs
    )
    return render(request, 'read/all_posts.html', context)

def post_detail_view(request, user_slug, post_slug):
    post = get_object_or_404(BlogPost, slug = post_slug, is_active=True)
    post.view_count += 1
    post.save()

    ids = request.user.userpostfav_set.filter(is_deleted=False).values_list('post_id', flat=True)
    favs=BlogPost.objects.filter(id__in=ids, is_active=True)

    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

            comment_form = CommentForm()


    context = dict(
        post = post,
        comment_form = comment_form,
        favs = favs
    )
    return render(request, 'read/post_detail.html', context)