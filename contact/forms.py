from django import forms
from .models import Contact
from django.utils import timezone
from datetime import timedelta


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("Email is required.")
        if "@" not in email or "." not in email.split("@")[-1]:
            raise forms.ValidationError("Enter a valid email address.")
        if len(email) > 254:
            raise forms.ValidationError(
                "Email address is too long. Maximum length is 254 characters."
            )
        two_hours_ago = timezone.now() - timedelta(hours=2)
        if Contact.objects.filter(email=email, created_at__gte=two_hours_ago).exists():
            raise forms.ValidationError(
                "You already messaged me. Please wait at least 2 hours before sending another message."
            )
        return email

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if not message:
            raise forms.ValidationError("Message is required.")
        return message
