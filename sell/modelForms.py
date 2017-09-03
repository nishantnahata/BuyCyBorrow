from django import forms

from borrow.models import Cycle


class sellForm(forms.ModelForm):

    class Meta:
        model = Cycle
        fields = ['photo','name','description','cost']

