import os
from django.db import models

# Create your models here.
class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Portfolio Category"
        verbose_name_plural = "Portfolio Categories"


def project_uploads(instance, filename):
    upload_path = "portfolio_images"
    return os.path.join(upload_path, filename.lower())


class Project(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200, blank=True, null=True)
    services = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(
        PortfolioCategory, on_delete=models.SET_NULL, null=True, blank=False
    )
    description = models.TextField(blank=True, null=True)
    default_img = models.ImageField(upload_to=project_uploads)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_images"
    )
    image = models.ImageField(upload_to=project_uploads)

    def __str__(self):
        return "{} - {}".format(self.project.name, self.id)
