from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.core.mail import send_mail


from .forms import (
    EstimateForm,
    ContactUsForm,
    FinancingForm,
    LandingEstimateForm,
)
from portfolio.models import Project

# Create your views here.


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estimate_form"] = EstimateForm()
        return context


class ResidentialLandingPage(TemplateView):
    template_name = "pages/landing_residential.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estimate_form"] = LandingEstimateForm()
        context["contact_form"] = ContactUsForm()
        context["projects"] = Project.objects.filter(category__name="Residential")[:9]
        return context


class ResidentialServicesView(TemplateView):
    template_name = "pages/residential.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estimate_form"] = EstimateForm()
        context["financing_form"] = FinancingForm()
        context["projects"] = Project.objects.filter(category__name="Residential")[:12]
        return context


class CommercialServicesView(TemplateView):
    template_name = "pages/commercial.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.filter(category__name="Commercial")[:12]
        return context


class AboutUsView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()[:8]
        return context


class ContactUsView(TemplateView):
    template_name = "pages/contact_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_form"] = ContactUsForm()
        return context


def estimate_request(request):
    data = dict()
    if request.method == "POST":
        form = EstimateForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            context = {
                "name": name,
                "email": email,
                "phone": form.cleaned_data["phone"],
                "requested_date": form.cleaned_data["requested_date"],
                "city": form.cleaned_data["city"],
                "state": form.cleaned_data["state"],
                "message": form.cleaned_data["message"],
            }

            ### SEND EMAIL ###

            template = get_template("pages/emails/estimate_request.txt")
            content = template.render(context)
            send_mail(
                "NEW ESTIMATE REQUEST",
                content,
                "{}<{}>".format(name, email),
                ["chad@exteriordd.com"],
                fail_silently=False,
            )

            data["html_success_message"] = render_to_string(
                "pages/includes/partial_estimate_submit_success.html", request=request,
            )
            data["form_is_valid"] = True

        else:
            data["form_is_valid"] = False
    else:
        estimate_form = EstimateForm()
        data["html_form"] = render_to_string(
            "pages/includes/partial_estimate_form.html",
            {"estimate_form": estimate_form},
            request=request,
        )
    return JsonResponse(data)


def financing_request(request):
    data = dict()
    if request.method == "POST":
        form = FinancingForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            context = {
                "name": name,
                "email": email,
                "phone": form.cleaned_data["phone"],
            }

            ### SEND EMAIL ###

            template = get_template("pages/emails/financing_request.txt")
            content = template.render(context)
            send_mail(
                "NEW FINANCING REQUEST",
                content,
                "{}<{}>".format(name, email),
                ["chad@exteriordd.com"],
                fail_silently=False,
            )

            data["html_success_message"] = render_to_string(
                "pages/includes/partial_financing_submit_success.html", request=request,
            )
            data["form_is_valid"] = True

        else:
            data["form_is_valid"] = False
    return JsonResponse(data)


def contact_us_form(request):
    data = dict()
    if request.method == "POST":
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            context = {
                "name": name,
                "email": email,
                "phone": phone,
                "message": form.cleaned_data["message"],
            }

            ### SEND EMAIL ###

            template = get_template("pages/emails/contact_us.txt")
            content = template.render(context)
            send_mail(
                "NEW CONTACT REQUEST",
                content,
                "{}<{}>".format(name, email),
                ["chad@exteriordd.com"],
                fail_silently=False,
            )

            data["html_success_message"] = render_to_string(
                "pages/includes/partial_contact_success.html", request=request,
            )
            data["form_is_valid"] = True

        else:
            data["form_is_valid"] = False
    return JsonResponse(data)
