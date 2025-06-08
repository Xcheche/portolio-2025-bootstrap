from django.db import models

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
    APP = 'app', 'App'
    WEB = 'web', 'Web'

class StatusChoices(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'


class Portfolio(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='portfolio_images/%Y/%m/%d/')
    preview_image = models.ImageField(upload_to='portfolio_preview_images/%Y/%m/%d/')
    project_url = models.URLField(max_length=300, blank=True, null=True)
    stack = models.CharField(max_length=300, blank=True, null=True)
    features_title = models.CharField(max_length=100, blank=True, null=True)
    features_description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CategoryChoices)
    status = models.CharField(max_length=20, choices=StatusChoices, default='draft')
    created = models.DateTimeField(auto_now_add=True)
    
    
    
    
    def __str__(self):
        return self.title
    # This method returns the string representation of the model instance, which is the title of the portfolio item.
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
        ordering = ['-created']
        
        # This will ensure that the portfolio items are ordered by their creation date in descending order.
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('portfolio:portfolio_detail', kwargs={'id': self.pk})
    
    
    
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='testimonials/%Y/%m/%d/', blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.role}"
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['-id']
        
        # This will ensure that the testimonials are ordered by their ID in descending order.    