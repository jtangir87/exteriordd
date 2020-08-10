from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import BlogCategory, BlogPost

# Create your views here.


def blog_list(request):
    blog_list = BlogPost.objects.filter(published=True)
    page = request.GET.get("page", 1)
    sidebar_blogs = BlogPost.objects.filter(published=True)[:5]
    categories = BlogCategory.objects.all()

    paginator = Paginator(blog_list, 10)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        "blogs": blogs,
        "sidebar_blogs": sidebar_blogs,
        "categories": categories,
    }

    return render(request, "blog/blog_list.html", context)


class BlogList(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = BlogPost.objects.filter(published=True)
        context["sidebar_blogs"] = BlogPost.objects.filter(published=True)[:5]
        context["categories"] = BlogCategory.objects.all()
        return context


def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)

    context = {
        "sidebar_blogs": BlogPost.objects.filter(published=True)[:5],
        "categories": BlogCategory.objects.all(),
        "blog": blog,
    }

    return render(request, "blog/blog_detail.html", context)