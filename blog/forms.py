from django import forms
from django.forms import ModelForm
from blog.models import Post

#Create a Form from a Model, since its basically the Model.
class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        #exclude the creation_date, as it will be auto generated
        exclude = ['creation_date']
    

#When editing a post, we don't need to edit the author, they still wrote it
#and we also don't need to edit the date it was created, it was still created then
#If our blog site was a good one though, we would have a "last edited" date field
class EditPostForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)
    