"""pages URL Configuration

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
from django.views.generic import TemplateView

from .views import (
    HomeView,
    estimate_request,
    ContactUsView,
    ResidentialServicesView,
    financing_request,
    ResidentialLandingPage,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact-us", ContactUsView.as_view(), name="contact_us",),
    path("free-estimate", estimate_request, name="estimate_request"),
    path("financing", financing_request, name="financing_request"),
    path(
        "about-us",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about_us",
    ),
    path("residential-services", ResidentialServicesView.as_view(), name="residential",),
    path(
        "commercial-services",
        TemplateView.as_view(template_name="pages/commercial.html"),
        name="commercial",
    ),

    ## LANDING PAGES ##
    path('residential', ResidentialLandingPage.as_view(), name="landing_residential"),
]
