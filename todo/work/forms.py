from django.forms import ModelForm
from .models import Work


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = '__all__'

class UpdateWorkForm(ModelForm):
    class Meta:
        model = Work
        fields = '__all__'        