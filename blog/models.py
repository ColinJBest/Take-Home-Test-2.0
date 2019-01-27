from django.db import models

# Author Model represents the Author of the post post, ala Tumblr people may enjoy reading certain post authors
class Author(models.Model):
    author_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=300)
    def __str__(self):
        return self.author_name + " Bio:" + self.bio

#Posts need to be associated with authors, so that users can read other postings by the same authors
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('date created')
    def __str__(self):
        return self.title

