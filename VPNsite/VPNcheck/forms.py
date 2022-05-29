from .models import Server
from django.forms import ModelForm


class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ['name']
