from modeltranslation.translator import register, TranslationOptions
from .models import Portfolio, About, Testimonial


@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "stack",
        "features_title",
        "features_description",
        "category",
        "project_status",
        "status",
        "project_url",
        "image",
        "preview_image",
    )


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "tech_stack",
        "qualifications",
        "bio",
        "blog_url",
        "social_links",
        "phone",
        "email",
    )


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ("name", "role", "message", "email", "rating", "image")
