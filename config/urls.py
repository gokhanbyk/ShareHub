"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from page.views import *
from blog.views import search_view

urlpatterns = [
    
    path('', home_view, name='home_view'),
    path('blog/', forum_page_view, name='forum_page_view'),

    # Search:
    path('search/', search_view, name='search_view'),

    # User
    path('user/', include('user.urls', namespace='user')),
    # Read
    path('read/', include('read.urls', namespace='read')),

    # Blog
    path('blog/', include('blog.urls', namespace='blog')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
