from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages

from security.forms import ContactForm, SubscribeForm

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
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            p = form.save()
            messages.success(request, "Your message has been sent. Thank you!")
            return redirect("contact")
        else:
            messages.error(request, "Your information was not submitted")
            

    context['form'] = form
    return render(request, 'basic/contact.html', context)


def calculator(request):
    context = dict()
    context['title'] = 'Calculator'
    return render(request, 'basic/calculator.html', context)


def portfolio(request):
    context = dict()
    context['title'] = 'Portfolio'
    return render(request, 'basic/portfolio.html', context)


def subcribe(request):
    context = {"title":"Subscribe" }
    form = SubscribeForm()
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            p = form.save()
            messages.success(request, "You have successfully subscribed to our newsletters!.")
            return redirect("home")
        else:
            messages.error(request, "Email address already taken, please use a different one!.")
            

    context['form'] = form
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))