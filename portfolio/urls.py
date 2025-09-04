from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    # Home
    path("", views.portfolio, name="portfolio"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:portfolio>/",
        views.portfolio_detail,
        name="portfolio_detail",
    ),
    # urls.py
    # about page
    path("about/", views.about, name="about"),
    # services page
    path("services/", views.services, name="services"),
    path("search/", views.portfolio_search, name="portfolio_search"),
]
