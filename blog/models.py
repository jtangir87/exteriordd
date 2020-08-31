import os
from django.db import models
from django.shortcuts import reverse

from autoslug import AutoSlugField
from tinymce.models import HTMLField

# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from="name")

    class Meta:
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def post_count(self):
        return BlogPost.objects.filter(categories=self, published=True).count()


def blog_uploads(instance, filename):
    upload_path = "blog_images"
    return os.path.join(upload_path, filename.lower())


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(BlogCategory)
    page_css = models.TextField(blank=True, null=True)
    header_img = models.ImageField(upload_to=blog_uploads)
    slug = AutoSlugField(populate_from="title")
    post = HTMLField()
    page_js = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"slug": self.slug})
