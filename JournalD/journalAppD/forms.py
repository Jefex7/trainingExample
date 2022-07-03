from datetime import datetime
from django.forms import ModelForm
from journalAppD.models import Resource

class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = ['date_created','title', 'content']

