from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class EstimateForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    requested_date = forms.DateField(
        widget=DatePickerInput(format="%m/%d/%Y"), required=False
    )
    city = forms.CharField(max_length=150, required=False)
    state = forms.CharField(max_length=100, required=False)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "How can we help?"}), required=False
    )
    address_hp = forms.CharField(
        max_length=50, required=False, widget=forms.HiddenInput())


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "How can we help?"})
    )
    address_hp = forms.CharField(
        max_length=50, required=False, widget=forms.HiddenInput())


class FinancingForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address_hp = forms.CharField(
        max_length=50, required=False, widget=forms.HiddenInput())


class LandingEstimateForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address_hp = forms.CharField(
        max_length=50, required=False, widget=forms.HiddenInput())
