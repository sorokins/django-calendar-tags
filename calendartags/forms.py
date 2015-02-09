from django import forms


class iCalendarForm(forms.Form):
    start_time = forms.DateTimeField(widget=forms.HiddenInput)
    end_time = forms.DateTimeField(widget=forms.HiddenInput)
    title = forms.CharField(max_length=1000, widget=forms.HiddenInput)
    description = forms.CharField(widget=forms.HiddenInput, required=False)
    url = forms.CharField(widget=forms.HiddenInput)
    address = forms.CharField(max_length=1000, widget=forms.HiddenInput, required=False)