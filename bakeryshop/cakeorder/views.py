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
    try:
        user_name = request.session['user_name']
        client = Customer.objects.get(name=user_name)
        name = client.name
    except:
        name = ''
    levels = Levels_number.objects.all()
    forms = Form.objects.all()
    toppings = Topping.objects.all()
    berries = Berries.objects.all()
    decors = Decor.objects.all()

    if request.method == 'GET':
        if request.GET:
            cake_id = request.GET.get('CAKE_ID')
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
            customer = Customer.objects.filter(phonenumber=phone)

            if cake_id:
                cake = Cake.objects.get(id=cake_id)
                form = cake.form
                levels_number = cake.levels_number
                topping = cake.topping
                decor = cake.decor
                berry = cake.berries
            else:
                form = forms.get(id=form_id)
                levels_number = levels.get(id=level_id)
                topping = toppings.get(id=topping_id)
                decor = decors.get_or_none(id=decor_id)
                berry = berries.get_or_none(id=berries_id)


            if customer:
                customer = customer.first()
                user_name = customer.name
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
                    mail=email,
                    address=address
                )
            login(request, user)
            request.session['user_name'] = customer.name
            request.session['user_phone'] = customer.phonenumber

            cake, _ = Cake.objects.get_or_create(
                price=form.price + levels_number.price + topping.price + get_price(decor) + get_price(berry),
                levels_number=levels_number,
                form=form,
                topping=topping,
                berries=berry,
                decor=decor,
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
        },
        'client': {
            'name': name}
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
    request.session['user_phone'] = client.phonenumber
    return redirect('lk')


def lk(request):
    try:
        user_name = request.session['user_name']
    except:
        return redirect('/')

    client = Customer.objects.get(name=user_name)
    orders = Order.objects.filter(customer=client)
    orders_con =[]
    if orders:
        for order in orders:
            order_con = {
                'numer': order.id,
                'cake': order.cake.name,
                'status': order.status,
                'delivery_time': order.delivery_time.strftime('%H:%M - %d %B')}
            orders_con.append(order_con)

    context = {
        'client': {
            'name': client.name,
            'phone': client.phonenumber,
            'mail': client.mail,
        },
        'orders': orders_con
    }

    return render(request, 'lk.html', context = context)


def catalog(request):
    try:
        user_name = request.session['user_name']
        client = Customer.objects.get(name=user_name)
        name = client.name
    except:
        name = ''
    cakes = Cake.objects.filter(type='CG')
    cakes_con =[]
    if cakes:
        for cake in cakes:
            cake_con = {
                'name': cake.name,
                'occasion': cake.get_occasion_display(),
                'img_url': cake.image.url,
                'price': cake.price,
                'type': cake.get_type_display(),
                'id': cake.id,
            }
            cakes_con.append(cake_con)

    context = {
        'client': {
            'name': name,
        },
        'cakes': cakes_con
    }
    print(context['cakes'])
    return render(request, 'catalog.html', context = context)


def sync_click(request):
    print(count_clicks())
    return redirect("/admin/cakeorder/advertisement/")

def get_price(row):
    try:
        return row.price
    except AttributeError as e:
        print(e)
        return 0
