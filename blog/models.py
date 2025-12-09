from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from users.models import Profile


# Create your models here.

class Post(models.Model):
    slug = models.SlugField(unique=True, blank=True, null=True)
    title = models.CharField(max_length=400)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True) #datefield only used to store year
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.ManyToManyField(Profile, related_name='post_likes', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate if slug is not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    date_added = models.DateTimeField(auto_now_add=True) #datetimefield used to store both year and times

    def is_reply(self):
        return self.parent is not None

    def __str__(self):
        return f"{self.post} - {self.body[:5]}"