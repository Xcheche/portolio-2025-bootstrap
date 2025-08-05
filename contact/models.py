from django.db import models

# Create your models here.


class Contact(models.Model):
    class SubjectChoices(models.TextChoices):
        PROJECT = "i have a project in mind", "I have a project in mind"
        COLLABORATION = (
            "i'm a developer looking for collaboration",
            "I'm a developer looking for collaboration",
        )
        RESUME = "i'm a recruiter", "I'm a recruiter"
        OTHER = "other", "Other"

    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(
        max_length=250,
        choices=[
            (SubjectChoices.PROJECT, "I have a project in mind"),
            (SubjectChoices.COLLABORATION, "I'm a developer looking for collaboration"),
            (SubjectChoices.RESUME, "I'm a recruiter"),
            (SubjectChoices.OTHER, "Other"),
        ],
        default=SubjectChoices.PROJECT,
        blank=False,
        null=False,
    )
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
