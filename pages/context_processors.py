from .forms import EstimateForm


def estimate_form_processor(request):
    estimate_form = EstimateForm()
    return {"estimate_form": estimate_form}

