from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
import os

def get_thumb_path(instance, filename):
    return os.path.join('images','thumbs', filename)


class Post_Thoughts(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(('slug'), max_length=60, blank=True)
    text = models.TextField()
    thumb = models.ImageField(upload_to=get_thumb_path, blank=True, null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post_Thoughts, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post_Work(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(('slug'), max_length=60, blank=True)
    text = models.TextField()
    thumb = models.ImageField(upload_to=get_thumb_path, blank=True, null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post_Work, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post_Photos(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(('slug'), max_length=60, blank=True)
    thumb = models.ImageField(upload_to=get_thumb_path, blank=True, null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post_Photos, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post_Videos(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(('slug'), max_length=60, blank=True)
    youtube = models.CharField(max_length=200)
    thumb = models.ImageField(upload_to=get_thumb_path, blank=True, null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post_Videos, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

