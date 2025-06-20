from django.contrib import admin
from .models import Portfolio,Testimonial

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created','category')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')
 
admin.site.register(Portfolio, PortfolioAdmin)




class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('name', 'role', 'message')
    list_editable = ('is_approved',)


admin.site.register(Testimonial,TestimonialAdmin)    