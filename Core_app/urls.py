from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_view, name='hero'),  # Set hero as root URL
    path('blog/', views.blog_view, name='blog'),
    path('faq/', views.faq_view, name='faq'),
    path('services/', views.services_view, name='services'),
    path('cta/', views.cta_view, name='cta'),
    path('contact/', views.contact_view, name='contact'),
    path('about-us/', views.about_us_view, name='about_us'),
]
