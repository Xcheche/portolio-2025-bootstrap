from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('',views.portfolio, name='portfolio'),
    path('portfolio_detail/<int:id>/', views.portfolio_detail, name='portfolio_detail'),
    # urls.py
   

    #about page
    path('about/', views.about, name='about'),
    #services page
    path('services/', views.services, name='services'),
]