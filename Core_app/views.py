from django.shortcuts import render

def blog_view(request):
    return render(request, 'Core_app/blog.html')

def faq_view(request):
    return render(request, 'Core_app/faq.html')

def hero_view(request):
    return render(request, 'Core_app/hero.html')

def services_view(request):
    return render(request, 'Core_app/services.html')

def cta_view(request):
    return render(request, 'Core_app/cta.html')

def contact_view(request):
    return render(request, 'Core_app/contact.html')

def about_us_view(request):
    return render(request, 'Core_app/about_us.html')


