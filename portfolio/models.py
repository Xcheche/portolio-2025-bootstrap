from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static

# Create your models here.


class CategoryChoices(models.TextChoices):
    APP = "app", _("App")
    WEB = "web", _("Web")


class StatusChoices(models.TextChoices):
    DRAFT = "draft", _("Draft")
    PUBLISHED = "published", _("Published")


class Portfolio(models.Model):
    title = models.CharField(
        max_length=100, blank=False, null=False, verbose_name=_("Title")
    )
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_("Slug"))
    image = models.ImageField(
        upload_to="portfolio_images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name=_("Image"),
    )
    preview_image = models.ImageField(
        upload_to="portfolio_preview_images/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name=_("Preview Image"),
    )
    project_url = models.URLField(
        max_length=300, blank=True, null=True, verbose_name=_("Project URL")
    )
    stack = models.CharField(
        max_length=300, blank=True, null=True, verbose_name=_("Stack")
    )
    features_title = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("Features Title")
    )
    features_description = models.TextField(
        blank=True, null=True, verbose_name=_("Features Description")
    )
    category = models.CharField(
        max_length=20, choices=CategoryChoices.choices, verbose_name=_("Category")
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default="draft",
        verbose_name=_("Status"),
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    project_status = models.CharField(
        max_length=20,
        choices=[("development", _("Development")), ("production", _("Production"))],
        default="production",
        verbose_name=_("Project Status"),
    )

    @property
    def image_url(self):
        if self.image and hasattr(self.image, "url"):
            return self.image.url
        else:
            return static("img/placeholder.png")

    def __str__(self):
        return self.title

    @property
    def preview_image_url(self):
        if self.preview_image and hasattr(self.preview_image, "url"):
            return self.preview_image.url
        else:
            return static("img/placeholder.png")  # optional

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")
        ordering = ["-created"]

    def get_absolute_url(self):

        return reverse(
            "portfolio:portfolio_detail",
            kwargs={
                "portfolio": self.slug,
                "year": self.created.year,
                "month": self.created.month,
                "day": self.created.day,
            },
        )


class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    email = models.EmailField(
        max_length=254, verbose_name=_("Email")
    )  # new email field
    role = models.CharField(max_length=100, blank=True, verbose_name=_("Role"))
    image = models.ImageField(
        upload_to="testimonials/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name=_("Image"),
    )
    message = models.TextField(verbose_name=_("Message"))
    rating = models.PositiveIntegerField(default=5, verbose_name=_("Rating"))
    is_approved = models.BooleanField(default=False, verbose_name=_("Is Approved"))

    def __str__(self):
        return f"{self.name} - {self.role}"

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")
        ordering = ["-id"]


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_("Slug"))
    qualifications = models.TextField(
        blank=True, null=True, verbose_name=_("Qualifications")
    )
    bio = models.TextField(blank=True, null=True, verbose_name=_("Bio"))
    blog_url = models.URLField(
        max_length=300, blank=True, null=True, verbose_name=_("Blog URL")
    )
    tech_stack = models.TextField(blank=True, null=True, verbose_name=_("Tech Stack"))
    phone = models.CharField(
        max_length=15, blank=True, null=True, verbose_name=_("Phone")
    )
    email = models.EmailField(blank=True, null=True, verbose_name=_("Email"))
    social_links = models.CharField(
        max_length=500, blank=True, null=True, verbose_name=_("Social Links")
    )  # Store social links as a JSON object
    image = models.ImageField(
        upload_to="about_images/%Y/%m/%d/", verbose_name=_("Image")
    )
    city = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("City")
    )
    freelance_status = models.CharField(
        max_length=20,
        choices=[("available", _("Available")), ("not_available", _("Not Available"))],
        default="available",
        verbose_name=_("Freelance Status"),
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("portfolio:about", kwargs={"about_slug": self.slug})
