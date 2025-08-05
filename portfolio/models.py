from django.db import models
from django.urls import reverse


# Create your models here.


# CategoryChoices = (
#     ('web', 'Web'),
#     ('app', 'App'),
# )
# StatusChoices = (
#     ('draft', 'Draft'),
#     ('published', 'Published'),


# )
class CategoryChoices(models.TextChoices):
    APP = "app", "App"
    WEB = "web", "Web"


class StatusChoices(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"


class Portfolio(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    #slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to="portfolio_images/%Y/%m/%d/")
    preview_image = models.ImageField(upload_to="portfolio_preview_images/%Y/%m/%d/")
    project_url = models.URLField(max_length=300, blank=True, null=True)
    stack = models.CharField(max_length=300, blank=True, null=True)
    features_title = models.CharField(max_length=100, blank=True, null=True)
    features_description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CategoryChoices)
    status = models.CharField(max_length=20, choices=StatusChoices, default="draft")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # This method returns the string representation of the model instance, which is the title of the portfolio item.
    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
        ordering = ["-created"]

        # This will ensure that the portfolio items are ordered by their creation date in descending order.

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("portfolio:portfolio_detail", kwargs={"id": self.pk})


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="testimonials/%Y/%m/%d/", blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.role}"

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ["-id"]

        # This will ensure that the testimonials are ordered by their ID in descending order.


# About
class About(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    qualifications = models.TextField(blank=True, null=True)

    bio = models.TextField(blank=True, null=True)
    blog_url = models.URLField(max_length=300, blank=True, null=True)
    tech_stack = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    social_links = models.CharField(
        max_length=500, blank=True, null=True
    )  # Store social links as a JSON object
    image = models.ImageField(upload_to="about_images/%Y/%m/%d/")
    city = models.CharField(max_length=100, blank=True, null=True)
    freelance_status = models.CharField(
        max_length=20,
        choices=[("available", "Available"), ("not_available", "Not Available")],
        default="available",
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"


    
    def get_absolute_url(self):
        # self.slug refers to the slug of THIS specific object
        from django.urls import reverse
        return reverse('portfolio:about', kwargs={'about_slug': self.slug})
