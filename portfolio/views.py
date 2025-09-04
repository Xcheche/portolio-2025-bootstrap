from time import time
from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404

# Pagination
from django.core.paginator import Paginator

# Models
from portfolio.models import Testimonial, Portfolio, About

# Forms
from portfolio.forms import TestimonialForm
from django.shortcuts import redirect

# Messages
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.http import require_GET
from django.core.mail import send_mail
from django.conf import settings

# Translations
from django.utils.translation import gettext as _


# Create your views here.


def portfolio(request):
    portfolios = Portfolio.objects.all().filter(status="published").order_by("-created")
    # Testimonials
    testimonials = Testimonial.objects.filter(is_approved=True).order_by("-id")[:2]
    # Pagination
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


def portfolio_detail(request, year, month, day, portfolio):
    try:
        portfolio = get_object_or_404(
            Portfolio,
            status="published",
            slug=portfolio,
            created__year=year,
            created__month=month,
            created__day=day,
        )
    except Http404:
        return render(request, "404.html", status=404)

    form = TestimonialForm()

    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = "New Testimonial Pending Approval"
            message = f"A new testimonial has been submitted by {form.instance.name} and is awaiting approval."
            admin_emails = [admin[1] for admin in settings.ADMINS]
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, admin_emails)
            return redirect(request.path)
        else:
            form = TestimonialForm()

    context = {
        "portfolio": portfolio,
        "form": form,
    }
    return render(request, "portfolio/portfolio_detail.html", context)


def services(request):
    return render(request, "portfolio/services.html")


# Search

def portfolio_search(request):
    import time  # noqa: F811

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




# =======Custom Error Handlers======

def custom_404_view(request, exception):
    return render(request, "404.html", status=404)


def custom_500_view(request):
    return render(request, "500.html", status=500)
