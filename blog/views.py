from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .forms import EditPostForm
from .forms import CreatePostForm
from .models import Author
from .models import Post

#Purpose: Display a list of blog postings
def index(request):
    a = Post.objects
    post_list = a.order_by('-creation_date')
    context = {'post_list':post_list }
    return render(request, 'blog/index.html',context)

#Purpose: display details of a Post, including the Author details
def details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post':post}
    return render(request, 'blog/detail.html', context)

#Purpose: Create a new Post
def creation(request):    
    #Creating an instance, since our ModelForm is excluding the creation_date
    dateOfPost = Post(creation_date= timezone.now())
    #Doing POST, as it is creation. Nothing to GET
    form = CreatePostForm(request.POST, instance=dateOfPost)

    if form.is_valid():
        #need to save the data
        new_post = form.save()
        #Redirect from the Creation-page to the successfully created page.
        return HttpResponseRedirect(reverse('detail', args=(new_post.id,)))
    #The Form as the context will generate our tables for creating
    context = {
        'form':form, 
    }
    #Render our page for input
    return render(request, 'blog/creation.html', context)

#Purpose: Allow the editing of the title and description of a Post.
def edit(request, post_id):
    editedPost = get_object_or_404(Post, pk=post_id)

    #We know we are doing POST
    form = EditPostForm(request.POST)
    #validate input
    if form.is_valid():
        editedPost.title = form.cleaned_data['title']
        editedPost.description = form.cleaned_data['description']
        editedPost.save()
        #Redirect from the Edit-page to the successfully edited page.
        return HttpResponseRedirect(reverse('detail', args=(post_id,)))
    
    #The Form as the context will generate our tables for editing
    context = {
        'form':form, 
    }
    #Render the page in order to allow input
    return render(request, 'blog/edit.html', context)