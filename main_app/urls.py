from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('memes/', views.memes_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('memes/user/', views.user_view, name='user'),
    path('memes/create/', views.MemeCreate.as_view(), name='memes_create'),
    path('memes/<int:pk>/update', views.MemeUpdate.as_view(), name='memes_update'),
    path('memes/<int:pk>/delete', views.MemeDelete.as_view(), name='memes_delete'),
    path('memes/user/<int:user_id>/', views.user_id, name='user_id'),
    path('memes/<int:meme_id>/like', views.like, name='like'),
    path('user/search', views.search, name='search'),
]