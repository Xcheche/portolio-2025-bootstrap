from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Testimonial


@receiver(post_save, sender=Testimonial)
def send_approval_notification(sender, instance, created, **kwargs):
    if not created and instance.is_approved:
        subject = "Your Testimonial Has Been Approved"
        message = "Thank you for your testimonial! It is now visible on the homepage."
        recipient = [instance.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient)
