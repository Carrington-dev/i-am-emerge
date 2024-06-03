from django.shortcuts import render

def home(request):
    context = dict()
    context['title'] = 'Home'
    return render(request, 'basic/home.html', context)


def about(request):
    context = dict()
    context['title'] = 'About'
    return render(request, 'basic/about.html', context)


def services(request):
    context = dict()
    context['title'] = 'Services'
    return render(request, 'basic/services.html', context)


def contact(request):
    context = dict()
    context['title'] = 'Contact'
    return render(request, 'basic/contact.html', context)


def calculator(request):
    context = dict()
    context['title'] = 'Calculator'
    return render(request, 'basic/calculator.html', context)


def portfolio(request):
    context = dict()
    context['title'] = 'Portfolio'
    return render(request, 'basic/portfolio.html', context)

