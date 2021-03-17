from django.db import models
from users.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    update_at = models.DateField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    url = models.URLField(max_length=2000)
    begin = models.TimeField(auto_now=False, auto_now_add=False)
    end = models.TimeField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=255)
    category = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Article(models.Model):
    ATTACHMENT_CHOICES = (
        ('pdf', 'Pdf'),
        ('image', 'Image'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    update_at = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=255)
    category = models.CharField(max_length=255)
    attachment = models.CharField(max_length=10,
                              choices=ATTACHMENT_CHOICES,
                              default='pdf'
                            )
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Information(models.Model):
    TYPES_CHOICES = (
        ('urgent', 'Urgent'),
        ('non_urgent', 'Non_urgent'),
    )
    ACCESS_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    ATTACHMENT_CHOICES = (
        ('pdf', 'Pdf'),
        ('image', 'Image'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    update_at = models.DateField(auto_now=False, auto_now_add=False)
    types = models.CharField(max_length=10,
                              choices=TYPES_CHOICES,
                              default='non_urgent'
                            )
    access = models.CharField(max_length=10,
                              choices=ACCESS_CHOICES,
                              default='public'
                            )
    attachment = models.CharField(max_length=10,
                              choices=ATTACHMENT_CHOICES,
                              default='pdf'
                            )                       
    image = models.ImageField(upload_to='Images/', height_field=None, width_field=None, max_length=255)
    video = models.FileField(upload_to='Vidéos/', null=True, verbose_name="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField()

