from django.contrib import admin
from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')
 
admin.site.register(Portfolio, PortfolioAdmin)