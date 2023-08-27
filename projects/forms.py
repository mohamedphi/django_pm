from django import forms
from . import models

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model=models.Project
        fields=["title","category","description"]
        widgets={
            'title':forms.TextInput(),
            'category':forms.Select(),
            'description':forms.Textarea()
        }