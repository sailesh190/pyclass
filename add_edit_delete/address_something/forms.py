from django import forms
from address_something import models

class addressform(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'