from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from accounts.models import Accounts
from .forms import *
# Create your views here.

categories = {
    'All': 'All',
    'Electronics': 'Electronics',
    'Furniture': 'Furniture',
    'Fashion': 'Fashion',
    'Books': 'Books',
    'Sports': 'Sports',
    'Services': 'Services',
    'Vehicles': 'Vehicles',
    'Food': 'Food'
}


def LNMshop_home(request):
    if not request.session.has_key('uid'):
        return redirect('login')
    products = Products.objects.all()
    context = {'categories': categories, 'products': products,
               'username': request.session['uid'], 'type': 'All'}
    if request.method == 'POST' and request.POST['category'] != 'All':
        products = Products.objects.filter(category=request.POST['category'])
        context['products'] = products
        context['type'] = request.POST['category']
    return render(request, 'LNMshop/LNMshop_home.html', context)


def view_product(request):
    if not request.session.has_key('uid'):
        return redirect('login')

    username = request.session['uid']
    user_products = Products.objects.filter(username_id=username)
    context = {'products': user_products, 'categories': categories,
               'username': request.session['uid']}
    return render(request, 'LNMshop/view_product.html', context)


def insert_product(request):
    if not request.session.has_key('uid'):
        return redirect('login')
    if request.method == 'POST':
        product = Products()
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.photo = request.FILES['photo']
        product.category = request.POST['category']
        product.contact_num = request.POST['contact_num']
        product.color = product.get_random_colour()
        product.username = Accounts(user_name=request.session['uid'])
        product.save()
        return redirect('LNMshop_home')
    account = Accounts.objects.get(user_name=request.session[('uid')])
    context = {'form': ProductForm(), 'categories': categories,
               'username': request.session['uid'], 'account': account}
    return render(request, 'LNMshop/insert_product.html', context)


def delete_product(request, id):
    product = Products.objects.filter(id=id)
    product.delete()
    username = request.session['uid']
    user_products = Products.objects.filter(username_id=username)
    context = {'products': user_products, 'username': request.session['uid']}
    return render(request, 'LNMshop/view_product.html', context)


def user_wishlist(request):
    username = request.session['uid']
    products = Wishlist.objects.filter(username_id=username)
    products = Products.objects.filter(
        id__in=products.values_list('product_id'))
    context = {'products': products, 'username': request.session['uid']}
    return render(request, 'LNMshop/user_wishlist.html', context)


def insert_wishlist(request, id):

    username = request.session['uid']
    products = Wishlist()
    products.username = Accounts(user_name=username)
    products.product = Products(id=id)

    context = {'categories': categories, 'products': Products.objects.all(
    ), 'username': request.session['uid'], 'type': 'All', }
    if username != Products.objects.filter(id=id)[0].username_id:
        products.save()

    return render(request, 'LNMshop/LNMshop_home.html', context)


def delete_wishlist_product(request, id):
    username = request.session['uid']
    product = Wishlist.objects.filter(product_id=id, username_id=username)
    product.delete()
    return user_wishlist(request)


def update_product(request):

    if request.method == 'POST':
        product = Products.objects.get(id=request.POST['id'])
        product_form = ProductForm(
            request.POST, request.FILES, instance=product)
        print(product_form)
        if product_form.is_valid():
            product_form.save()

    return redirect('view_product')
