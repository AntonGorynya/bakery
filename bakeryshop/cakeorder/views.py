from django.shortcuts import render, loader, HttpResponse, redirect
from .models import Levels_number, Form, Topping, Berries, Decor, Customer
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods


def index(request):
    levels = Levels_number.objects.all()
    forms = Form.objects.all()
    toppings = Topping.objects.all()
    berries = Berries.objects.all()
    decors = Decor.objects.all()

    context = {
        'data': {
            'levels': [level.quantity for level in levels],
            'forms': forms,
            'toppings': toppings,
            'berries': berries,
            'decors': decors,
        },
        'names': {
            'levels': ['не выбрано'] + [level.quantity for level in levels],
            'forms': ['не выбрано'] + [form.name for form in forms],
            'toppings': ['не выбрано'] + [topping.name for topping in toppings],
            'berries': ['не выбрано'] + [berry.name for berry in berries],
            'decors': ['не выбрано'] + [decor.name for decor in decors],
        },
        'costs': {
            'levels': [0] + [level.price for level in levels],
            'forms': [0] + [form.price for form in forms],
            'toppings': [0] + [topping.price for topping in toppings],
            'berries': [0] + [berry.price for berry in berries],
            'decors': [0] + [decor.price for decor in decors],
        }
    }

    return render(request, 'index.html', context=context)


@require_http_methods(['POST'])
def login_page(request):
    payload = dict(request.POST.items())
    phone = payload['REG']
    try:
        client = Customer.objects.get(phonenumber=phone)
        user = authenticate(username=client.name, password='password')
    except:
        user = None

    if not user:
        user = User.objects.create_user(
            username=phone,
            password='password'
        )

    login(request, user)
    client, created = Customer.objects.get_or_create(
        name=user,
        phonenumber=phone,
    )

    return redirect('lk')


def lk(request):
    name = request.user
    client = Customer.objects.get(name=name)
    context = {'client': {'user': client.name,
                        'phone': client.phonenumber,
                        'mail': client.mail,
                        },
                }
    print(context)

    return render(request, 'lk.html', context=context)


def lk_order(request):
    context = {}
    template = loader.get_template('lk-order.html')
    return HttpResponse(template.render(context))
