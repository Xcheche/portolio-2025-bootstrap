from django.shortcuts import render
from .forms import ContactForm
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.conf import settings

# Multi email


# Create your views here.


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or show a success messagen after saving the form or use messages framework
            # EMail sending logic can be added here if needed

            # Send email to site owner
            send_mail(
                subject="New Contact Form Submission",
                message=f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Send thank you email to user
            send_mail(
                subject="Thank you for contacting me",
                message="Thank you for your enquiry. I have received your message and will get back to you soon.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[form.cleaned_data["email"]],
                fail_silently=False,
            )
            return render(request, "contact/success.html")

    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})

# =======Custom Error Handlers======
def custom_404_view(request, exception):
    return render(request, "404.html", status=404)


def custom_500_view(request):
    return render(request, "500.html", status=500)
