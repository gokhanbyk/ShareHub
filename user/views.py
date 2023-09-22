from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from slugify import slugify
from .models import Profile
from .forms import *
from blog.models import BlogPost

# Create your views here.

login_required(login_url='user:login_view')
def show_user_fav_view(request):
    ids = request.user.userpostfav_set.filter(is_deleted=False).values_list('post_id', flat=True).order_by('-updated_at')
    
    
    context = dict(
        title = "Favorites",
        favs=BlogPost.objects.filter(id__in=ids, is_active=True)
    )    

    return render(request, 'blog/post_list.html', context)



login_required(login_url='user:login_view')
def profile_edit_view(request):
    user = request.user
    initial_data = dict(
        first_name = user.first_name,
        last_name = user.last_name,
    )
    form = ProfileModelForm(instance=user.profile, initial=initial_data)

    if request.method == 'POST':
        form = ProfileModelForm(
            request.POST or None,
            request.FILES or None,
            instance=user.profile,
        )
        if form.is_valid():
            f = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            f.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('home_view')


    title = 'Profili Düzenle: '
    context = dict(
        form = form,
        title = title,
    )
    return render(request, 'comon_components/form.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            username = User.objects.get(email = email).username

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home_view')
            else:
                return render(request, 'user/login.html', {
                    'form':form
                })
        else:
            return render(request, 'user/login.html', {
                'form':form
            })
    
    form = UserLoginForm()
    return render(request, 'user/login.html', {
        'form':form
    })

def logout_view(request):
    messages.info(request, f'{request.user.username} The session has been logged out.')    
    logout(request)
    return redirect('home_view')   

def register_view(request):
    if request.method == 'POST':
        post_info = request.POST
        email = post_info.get('email')
        email_confirm = post_info.get('email_confirm')
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_name')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        username = post_info.get('instagram')

        if len(first_name) < 3 or len(last_name) < 3 or len(email) < 3 or len(password) < 3:
            messages.warning(request, 'Information must be at least 3 characters long.')
            return redirect('user:register_view')
        if email != email_confirm:
            messages.warning(request, 'Please enter the email information correctly.')
            return redirect('user:register_view')
        if password != password_confirm:
            messages.warning(request, 'Please enter the password information correctly.')
            return redirect('user:register_view')
        
        user, created = User.objects.get_or_create(username = email) 
        if not created:
            user = authenticate(request, username = email, password = password)
            if user is not None:
                messages.success(request, '"You have already registered before. You have been redirected to the homepage.')
                login(request, user)
                return redirect('home_view')
            messages.warning(request, f'{email} The address is registered in the system, but you are not logged in. You are being redirected to the login page.')
            return redirect('user:login_view')
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        
        profile, profile_created = Profile.objects.get_or_create(user = user)
        profile.instagram = username
        profile.slug = slugify(f'{first_name}-{last_name}')
        
        user.save()
        profile.save()

        messages.success(request, f'{user.first_name} You have been registered in the system.')
        user = authenticate(request, username = email, password = password)
        login(request, user)
        return redirect('home_view')

    context = dict()
    return render(request, 'user/register.html', context)