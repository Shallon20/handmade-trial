from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from magic.compat import none_magic

from my_app.app_forms import ProductForm, LoginForm
from my_app.models import Product, CartItem


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'about.html', {'products': products})


def product(request):
    # data = Product.objects.all().order_by('-product_id').values()  # select * from customers
    # paginator = Paginator(data, 15)
    # page_number = request.GET.get('page', 1)
    # try:
    #     paginated_data = paginator.page(page_number)
    # except PageNotAnInteger | EmptyPage:
    #     paginated_data = paginator.page(1)
    # return render(request, 'products.html', {"data": paginated_data})
    return render(request, 'products.html')

def cart(request):
    cart_items = CartItem.objects.all()
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


def checkout(request):
    if request.method == 'POST':
        # M-pesa intergration logic
        pass
    return render(request, 'checkout.html')


def search_product(request):
    search_term = request.GET.get('search')
    data = Product.objects.filter( Q(name__icontains=search_term))
    return render(request, 'search.html', {"products": data})


def login_user(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)  # sessions stored on server # cookies stored in browser
                return redirect('customers')
        messages.error(request, "Invalid username or password")
        return render(request, 'login.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('login')


# def product_details(request):
#     customer = Customer.objects.get(id=customer_id)
#     deposits = customer.deposits.all()
#     total = Deposit.objects.filter(customer=customer).filter(status=True).aggregate(Sum('amount'))['amount__sum']
#     return render(request, "details.html", {"customer": customer, "deposits": deposits, "total": total})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product {form.cleaned_data['name']} was added")
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {"form": form})


def delete_product(request, product_id):
    products = Product.objects.get(id=product_id)
    products.delete()
    messages.info(request, f"Product {products.name} was deleted")
    return redirect('products')


def update_product(request, product_id):
    products = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product {form.cleaned_data['name']} was updated")
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_update.html', {"form": form, "products": products})


def product_details(request, product_id):
    products = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        CartItem.objects.create(product=product, quantity=request.POST['quantity'])
        return redirect('cart')
    return render(request, 'shop/product_details.html', {'products': products})