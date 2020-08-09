"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import ResidentialProjectList, CommercialProjectList, ProjectDetail

app_name = "portfolio"

urlpatterns = [
    path("residential", ResidentialProjectList.as_view(), name="residential_projects"),
    path("commercial", CommercialProjectList.as_view(), name="commercial_projects"),
    path("<int:pk>", ProjectDetail.as_view(), name="project_detail"),
]

