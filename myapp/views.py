from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Product, Client, Order
from .forms import ProductForm, ProductFilterForm, ProductPhotoForm, OrderForm


def index(request):
    return render(request, 'index.html')

def order(request):
    return render(request, 'order.html')

def product(request):
    return render(request, 'product.html')

def client(request):
    return render(request, 'client.html')

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product/product_detail', product_id=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product/product_form.html', {'form': form})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)
def client_orders(request, client_id, days):
    client = Client.objects.get(pk=client_id)
    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)

    orders = Order.objects.filter(client=client, order_date__gte=start_date, order_date__lte=end_date)
    products = []

    for order in orders:
        products.extend(order.products.all())

    # Исключение дубликатов товара
    unique_products = list(set(products))

    context = {
        'client': client,
        'unique_products': unique_products,
        'days': days,
    }

    return render(request, 'client/client_orders.html', context)

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order_detail.html', {'order': order})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})


from django.shortcuts import render, redirect
from .forms import OrderForm


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_amount = sum(product.price for product in form.cleaned_data['products'])
            order.save()
            order.products.set(form.cleaned_data['products'])  # Связываем выбранные товары с заказом

            return redirect('order/order_list')
    else:
        form = OrderForm()

    return render(request, 'order/order_form.html', {'form': form})



def all_products(request):
    products = Product.objects.all()
    filter_form = ProductFilterForm(request.GET)
    photo_form = ProductPhotoForm()

    if filter_form.is_valid():

        return render(request, 'product/all_products.html', {'products': products, 'filter_form': filter_form, 'photo_form': photo_form})

def client_detail(request, client_id):
    client = Client.objects.get(pk=client_id)
    return render(request, 'client/client_detail.html', {'client': client})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/client_list.html', {'clients': clients})

