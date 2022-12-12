from django import forms
from .models import DocumentPer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = DocumentPer
        fields = ['doc_name', 'path']
