from django.shortcuts import render, get_object_or_404

from portfolio.models import Testimonial, Portfolio
from portfolio.forms import TestimonialForm
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects.all().filter(status='published').order_by('-created')
    testimonials = Testimonial.objects.filter(is_approved=True)[:7]  # Fetch only the first 5 approved testimonials
    # If you want to limit the number of testimonials displayed, you can use slicing
    # testimonials = testimonials[:5]  # Display only the first 5 testimonials
    
    
    context = {
       
        'portfolios': portfolios,
        'testimonials': testimonials,
    }

    return render(request, 'portfolio/portfolio.html', context)



def portfolio_detail(request,id):
    portfolio = get_object_or_404(Portfolio, id=id, status='published')
    
    
    
    # Create a new testimonial form instance
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # is_approved stays False by default
            messages.success(request, 'Your testimonial has been submitted and is awaiting approval. Check home page for updates.')
            return redirect('/')  # refresh page

    context = {
        'portfolio': portfolio,
        
        'form': form,# Testimonial form instance
    }
    return render(request, 'portfolio/portfolio_detail.html', context)










def about(request):
    return render(request, 'portfolio/about.html')



def services(request):
    return render(request, 'portfolio/services.html')



#Testitmonial

