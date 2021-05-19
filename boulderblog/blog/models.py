from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    country = models.CharField(max_length=255, unique=True)
    #region = models.CharField(max_length=255)

    #admin page = post: title + author
    def __str__(self):
        return self.country

    #required to return to specific url after function(creating a post)
    def get_absolute_url(self):
        #return reverse('post-detail', args=(str(self.id)))
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=255)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255 )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    country = models.CharField(max_length=255, default='uncategorised')
    likes = models.ManyToManyField(User, related_name='blog_post')
    dislikes = models.ManyToManyField(User, related_name='blog_dislike')
    grades = models.CharField(max_length=255, default='1')


    #display counter for likes on post
    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    #admin page = post: title + author
    def __str__(self):
        return self.title + ' | '+ str(self.author)

    #required to return to specific url after function(creating a post)
    def get_absolute_url(self):
        #return reverse('post-detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)




class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')
