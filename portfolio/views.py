from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Project

# Create your views here.
class ResidentialProjectList(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "portfolio/residential_list.html"

    def get_queryset(self):
        queryset = Project.objects.filter(category__name="Residential")
        return queryset


class CommercialProjectList(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "portfolio/commercial_list.html"

    def get_queryset(self):
        queryset = Project.objects.filter(category__name="Commercial")
        return queryset


class ProjectDetail(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "portfolio/project_detail.html"

