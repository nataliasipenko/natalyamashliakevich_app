from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    STATUS = (
        (0, "Drafted"),
        (1, "Published"),
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)


class ClientPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    file = models.FileField(upload_to='media')
    author = models.CharField(max_length=80)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         "posts:detail",
    #         kwargs={
    #             "pk": self.id,
    #         }
    #     )


class Contactmessage(models.Model):
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=5550)

    def __str__(self):
        return self.email
