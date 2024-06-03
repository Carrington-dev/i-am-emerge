from django.urls import path

from security import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('calculator', views.calculator, name='calculator'),
    path('services', views.services, name='services'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
]
