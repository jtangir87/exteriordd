from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import BlogPost


class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            "about_us",
            "contact_us",
            "residential",
            "commercial",
            "landing_residential",
            "blog:blog_list",
        ]

    def location(self, item):
        return reverse(item)


class BlogPostSitemap(Sitemap):
    def items(self):
        return BlogPost.objects.filter(published=True)
