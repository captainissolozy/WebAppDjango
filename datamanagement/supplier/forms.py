from django import forms
from .models import DocumentPer


class SupplierForm(forms.ModelForm):

    class Meta:
        model = DocumentPer
        fields = ['doc_name', 'path']
