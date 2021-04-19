from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text="Enter first name")
    last_name = forms.CharField(max_length=50, required=False, help_text="Enter last name")
    email = forms.EmailField(max_length=200, help_text="Required. Inform a valid email address")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'place', 'tags', 'all_day', 'created_by', 'date', 'time_start', 'time_end', 'type_of_place', 'description')

    def clean(self):
        if self.cleaned_data['all_day']:
            self.cleaned_data['time_start'] = ''
            self.cleaned_data['time_end'] = ''

        return self.cleaned_data
