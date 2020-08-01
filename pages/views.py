from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import EstimateForm, ContactUsForm, FinancingForm

# Create your views here.


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estimate_form"] = EstimateForm()
        return context


class ResidentialServicesView(TemplateView):
    template_name = "pages/residential.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estimate_form"] = EstimateForm()
        context["financing_form"] = FinancingForm()
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
            context = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "phone": form.cleaned_data["phone"],
                "requested_date": form.cleaned_data["requested_date"],
                "city": form.cleaned_data["city"],
                "state": form.cleaned_data["state"],
                "message": form.cleaned_data["message"],
            }

            ### SEND EMAIL ###

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
            context = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "phone": form.cleaned_data["phone"],
            }

            ### SEND EMAIL ###

            data["html_success_message"] = render_to_string(
                "pages/includes/partial_financing_submit_success.html", request=request,
            )
            data["form_is_valid"] = True

        else:
            data["form_is_valid"] = False
    return JsonResponse(data)
