from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('memes/', views.memes_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('memes/user/', views.user_view, name='user'),
]