from django import forms
from django.forms import fields

from movies_mbe.models import Movie, ShowTime


class DateInput(forms.DateInput):
    input_type      = "date"
    format          = ('%d-%m-%Y')


class MovieForm(forms.ModelForm):
    name            = forms.CharField(max_length=150)
    description     = forms.Textarea()
    released_date   = forms.DateField(widget=DateInput)

    class Meta:
        model = Movie
        fields = ['name', 'description', 'released_date']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 10}),
        }


class DateTimeInput(forms.DateTimeInput):
    input_type      = "datetime-local"
    format          = ['%Y-%m-%d %H:%M:%S']


class ShowTimeForm(forms.ModelForm):
    # name            = forms.CharField(max_length=150)

    timing          = forms.DateTimeField(widget=DateTimeInput)
    location        = forms.CharField(max_length=500)

    class Meta:
        model = ShowTime
        fields = ['timing', 'location']
