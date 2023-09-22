from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_post_view, name='create_blog_post_view'),
    path('category/<slug:category_slug>/', category_view, name='category_view'),
    path('tag/<slug:tag_slug>/', tag_view, name='tag_view'),
    path('post/<slug:post_slug>/edit/', post_edit_view, name='post_edit_view'),
    path('post/<slug:post_slug>/delete/', delete_post, name='delete_post_view'),
    path('fav-update/', fav_update, name='fav_update'),
]
