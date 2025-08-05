from django import forms
from portfolio.models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "role", "image", "message", "rating"]
