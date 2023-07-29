from django.shortcuts import render, loader, HttpResponse, redirect
from .models import Levels_number, Form, Topping, Berries, Decor, Customer, Cake, Order
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from .management.commands.count_clicks import count_clicks
from datetime import datetime
from django.contrib import admin
from django.shortcuts import redirect


def index(request):
    levels = Levels_number.objects.all()
    forms = Form.objects.all()
    toppings = Topping.objects.all()
    berries = Berries.objects.all()
    decors = Decor.objects.all()

    if request.method == 'GET':
        if request.GET:
            level_id = request.GET.get('LEVELS')
            form_id = request.GET.get('FORM')
            topping_id = request.GET.get('TOPPING')
            berries_id = request.GET.get('BERRIES')
            decor_id = request.GET.get('DECOR')
            words = request.GET.get('WORDS')
            comment = request.GET.get('COMMENTS')
            email = request.GET.get('EMAIL')
            address = request.GET.get('ADDRESS')
            delivery_date = request.GET.get('DATE')
            delivery_time = request.GET.get('TIME')
            delivery_comments = request.GET.get('DELIVCOMMENTS')
            phone = request.GET.get('PHONE')
            user_name = request.GET.get('NAME')
            client = Customer.objects.filter(phonenumber=phone)
            if client:
                client = client.first()
                user_name = client.name
            user_login = f'{user_name}{phone}'

            try:
                user = authenticate(username=user_login,
                                    password='password')
            except:
                user = None
            if not user:
                user = User.objects.create_user(
                    username=user_login,
                    password='password',
                )
            customer, created = Customer.objects.get_or_create(
                client=user,
                phonenumber=phone,
                name=user_name,
                mail=email
            )

            cake, _ = Cake.objects.get_or_create(
                price='100',
                levels_number=levels.get(id=level_id),
                form=forms.get(id=form_id),
                topping=toppings.get(id=topping_id),
                berries=berries.get_or_none(id=berries_id),
                decor=decors.get_or_none(id=decor_id),
                sign=words
            )
            order, _ = Order.objects.get_or_create(
                cake=cake,
                customer=customer,
                delivery_time=datetime.strptime(f'{delivery_date} {delivery_time}', '%Y-%m-%d %H:%M'),
                comment=comment,
                delivery_comment=delivery_comments
            )

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
        user_login = f'{client.name}{phone}'
        user = authenticate(username=user_login, password='password')
    except:
        user = None

    if not user:
        return redirect('index')

    login(request, user)
    request.session['user_name'] = client.name
    return redirect('lk')


def lk(request):
    user_name = request.session['user_name']
    client = Customer.objects.get(name=user_name)
    orders = Order.objects.filter(customer=client)
    orders_con =[]
    if orders:
        for order in orders:
            print(order.id)
            order_con = {
                'numer': order.id,
                'cake': order.cake,
                'status': order.status,
                'delivery_time': order.delivery_time.strftime('%H:%M - %d %B')}
            orders_con.append(order_con)

    context = {
        'client': {
            'user': client.name,
            'phone': client.phonenumber,
            'mail': client.mail,
        },
        'orders': orders_con
    }

    return render(request, 'lk.html', context = context)


def sync_click(request):
    print(count_clicks())
    return redirect("/admin/cakeorder/advertisement/")
