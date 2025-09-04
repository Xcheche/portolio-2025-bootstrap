from django import forms
from django.utils.translation import gettext_lazy as _
from portfolio.models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "email", "role", "image", "message", "rating"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': _('Your Name')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Your Email')}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your Role')}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Your Message')}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Your Rating')}),
        }
