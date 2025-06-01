from django.shortcuts import render, get_object_or_404

from portfolio.models import Portfolio

# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects.all().filter(status='published').order_by('-created')
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'portfolio/portfolio.html', context)



def portfolio_detail(request,id):
    portfolio = get_object_or_404(Portfolio, id=id, status='published')
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'portfolio/portfolio_detail.html', context)



def about(request):
    return render(request, 'portfolio/about.html')



def services(request):
    return render(request, 'portfolio/services.html')