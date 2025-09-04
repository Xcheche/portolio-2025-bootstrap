from django.contrib import admin
from .models import Portfolio, Testimonial, About
from portfolio import models
from modeltranslation.admin import TranslationAdmin


class AbouttInline(admin.TabularInline):
    model = models.About
    extra = 1


class PortfolioAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ("title", "status", "created", "category", "project_status")
    list_filter = ("status", "category", "project_status")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("status", "category", "project_status")


admin.site.register(Portfolio, PortfolioAdmin)


class TestimonialAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ("name", "role", "rating", "is_approved")
    list_filter = ("is_approved",)
    search_fields = ("name", "role", "message")
    list_editable = ("is_approved",)


admin.site.register(Testimonial, TestimonialAdmin)


class AboutAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ("title", "freelance_status", "created", "bio")
    list_filter = ("freelance_status", "bio")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "bio")
    list_editable = ("freelance_status",)


admin.site.register(About, AboutAdmin)
