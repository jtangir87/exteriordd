from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class EstimateForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    requested_date = forms.DateField(widget=DatePickerInput(format="%m/%d/%Y"))
    city = forms.CharField(max_length=150)
    state = forms.CharField(max_length=100)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "How can we help?"})
    )


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "How can we help?"})
    )

