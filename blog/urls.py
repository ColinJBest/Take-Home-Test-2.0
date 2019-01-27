from django.urls import path

from . import views

urlpatterns = [
    #Viewing a list of posts
    path('', views.index, name='index'),
    #Viewing the post
    path('blog/<int:post_id>/', views.details, name='detail'),
    #Editing the post
    path('blog/<int:post_id>/edit/', views.edit, name='edit'),
    #Creating a post
    path('blog/creation', views.creation,name='creation'),
]