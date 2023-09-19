from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('profile/edit/', profile_edit_view, name='profile_edit_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),
    path('favs/', show_user_fav_view, name='show_user_fav_view'),
]
