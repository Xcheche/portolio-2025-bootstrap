from time import time
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from portfolio.models import Testimonial, Portfolio, About
from portfolio.forms import TestimonialForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.http import require_GET

# Create your views here.


def portfolio(request):
    portfolios = Portfolio.objects.all().filter(status="published").order_by("-created")
    testimonials = Testimonial.objects.filter(is_approved=True).order_by("-id")[:2]
    paginator = Paginator(portfolios, 2)  # Paginate with 2 items per page
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {
        "portfolios": page_obj,  # Pass only the paginated page object
        "testimonials": testimonials,
        "paginator": paginator,
        "page_obj": page_obj,
    }

    return render(request, "portfolio/portfolio.html", context)


def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id, status="published")

    # Create a new testimonial form instance
    form = TestimonialForm()

    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # is_approved stays False by default
            # messages.success(request, 'Your testimonial has been submitted and is awaiting approval.')

            # send email to admin

            return redirect(request.path)  # using ajax
        else:
            form = TestimonialForm()

    context = {
        "portfolio": portfolio,
        "form": form,  # Testimonial form instance
    }
    return render(request, "portfolio/portfolio_detail.html", context)


def services(request):
    return render(request, "portfolio/services.html")


# Search


def portfolio_search(request):
    import time

    time.sleep(3)
    query = request.GET.get("q", "")
    portfolios = Portfolio.objects.filter(
        Q(title__icontains=query) | Q(features_description__icontains=query)
    ).order_by("-created")

    paginator = Paginator(portfolios, 2)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    context = {
        "portfolios": page_obj,
        "query": query,
        "paginator": paginator,
        "page_obj": page_obj,
    }

    if not portfolios.exists():
        context["message"] = "No portfolios found."

    return render(request, "portfolio/portfolio.html", context)


# About



def about(request):
    about_me = About.objects.all()
    context = {"about_me": about_me}
    return render(request, "portfolio/about.html", context)