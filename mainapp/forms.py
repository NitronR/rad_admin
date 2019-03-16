from django import forms
from mainapp.models import AccidentAlert


class AlertForm(forms.ModelForm):

    class Meta:
        model = AccidentAlert
        fields = '__all__'