from django.contrib import admin
from .models import PortfolioCategory, Project, ProjectImage

# Register your models here.
admin.site.register(PortfolioCategory)
admin.site.register(Project)
admin.site.register(ProjectImage)
