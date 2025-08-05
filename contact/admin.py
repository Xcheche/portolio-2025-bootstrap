from django.contrib import admin
from .models import Contact
from contact import models

# Register your models here.


class ContactInline(admin.TabularInline):
    model = models.Contact
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject")
    search_fields = ("name", "email", "subject")


admin.site.register(Contact, ContactAdmin)
