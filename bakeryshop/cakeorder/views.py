from django.shortcuts import render, loader, HttpResponse
from .models import Levels_number, Form, Topping, Berries, Decor


def index(request):
    context = {
        'levels': [level.quantity for level in Levels_number.objects.all()],
        'forms': [form for form in Form.objects.all()],
        'toppings': [topping for topping in Topping.objects.all()],
        'berries': [berry for berry in Berries.objects.all()],
        'decors': [decor for decor in Decor.objects.all()],
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))


def lk(request):
    context = {}
    template = loader.get_template('lk.html')
    return HttpResponse(template.render(context))


def lk_order(request):
    context = {}
    template = loader.get_template('lk-order.html')
    return HttpResponse(template.render(context))
