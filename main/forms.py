import re

from django import forms

from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["last_name", "first_name", "phone", "school_class"]
        widgets = {
            "last_name": forms.TextInput(attrs={"placeholder": "Иванов", "autocomplete": "family-name"}),
            "first_name": forms.TextInput(attrs={"placeholder": "Алмаз", "autocomplete": "given-name"}),
            "phone": forms.TextInput(attrs={"type": "tel", "placeholder": "+996 555 123 456", "inputmode": "tel", "autocomplete": "tel"}),
            "school_class": forms.TextInput(attrs={"placeholder": "7А"}),
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        if len(re.sub(r"\D", "", phone)) < 9:
            raise forms.ValidationError("Введите номер полностью, например +996 555 123 456")
        return phone

    def clean_last_name(self):
        return self.cleaned_data["last_name"].strip().capitalize()

    def clean_first_name(self):
        return self.cleaned_data["first_name"].strip().capitalize()

    def clean_school_class(self):
        return self.cleaned_data["school_class"].strip().upper()
