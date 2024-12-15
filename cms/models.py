from django.contrib.auth.models import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager
from website_backend.model_mixin import ModelMixin
from django.template.defaultfilters import slugify
from django.utils.text import slugify


class Category(ModelMixin):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = CKEditor5Field(null=True, blank=True)

    def __str__(self):
        return self.name


class State(ModelMixin):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(ModelMixin):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = CKEditor5Field(null=True, blank=True)

    def __str__(self):
        return self.name


class NewsDetail(ModelMixin):
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_keyword = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    outer_page_info = CKEditor5Field(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    image_description = models.TextField(null=True, blank=True)
    content = CKEditor5Field()
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class HomePageP1(ModelMixin):
    news_detail = models.ForeignKey(NewsDetail, on_delete=models.CASCADE)
    is_p1 = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_breaking = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.news_detail.title} - P1: {self.is_p1}, Popular: {self.is_popular}, Breaking: {self.is_breaking}"