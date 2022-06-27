from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone, dateformat
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Max
import random

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=20, default="-")
    def __str__(self):
        return self.name
    
class TimeTracker(models.Model):
    todaystart = models.DateTimeField(default=timezone.now)
    switch = models.BooleanField(default=False)

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    body = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    working = models.BooleanField(default=True)
    deadline = models.BooleanField(default=False)
    deadline_date = models.DateTimeField(default=timezone.now)
    project_date = models.CharField(max_length=100, default="-")
    client = models.CharField(max_length=100, default="-")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    profile_pic = models.ImageField(blank=True, upload_to="blog/profile_pic")
    photo = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")
    rough_pic = models.ImageField(blank=True, upload_to="blog/rough")

    @property
    def get_rough_pic_url(self):
        if self.rough_pic and hasattr(self.rough_pic, 'url'):
            return self.rough_pic.url
        else:
            return "/static/img/random.jpg"

    @property
    def get_profile_pic_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/img/random.jpg"

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        elif self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        elif self.rough_pic and hasattr(self.rough_pic, 'url'):
            return self.rough_pic.url
        else:
            return "/static/img/random.jpg"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default=1)
    comment_thumbnail_url = models.TextField(max_length=300, default="http://nowhere")
    comment_textfield = models.TextField()

class Pinterest(models.Model):
    pin_url = models.TextField(max_length=300, null=True)
    pin_img = models.ImageField(blank=True, upload_to="pin/%Y/%m/%d")

class RKGK(models.Model):
    RKGK_img = models.ImageField(blank=True, upload_to="pin/%Y/%m/%d")

    def get_random():
        max_id = RKGK.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            rkgk = RKGK.objects.filter(pk=pk).first()
        if rkgk:
              return rkgk
