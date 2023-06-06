from django.http import HttpResponse
from django.shortcuts import render
from category.models import Category
from store.models import Product
from django.contrib.auth.models import User
from .forms import Registerform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product
from Cart.models import CartItem, Cart
from django.core.exceptions import ObjectDoesNotExist
from Cart.views import _cart_id


def Home(request):
    products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.all()  # select * from Category
    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context)
def Register(request):
    if request.method=="POST":
        a=Registerform(request.POST)
        if a.is_valid():
            a.save()
    else:
        a=Registerform()
    return render(request,'Register.html',{'a':a})



def Signin(request,total=0,quantity=0,cart_items=None):
    if request.method=="POST":
        x=AuthenticationForm(request=request,data=request.POST)
        if x.is_valid():
            uname=x.cleaned_data['email']
            upass=x.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
            return render(request,'Signin.html')
    else:
        x=AuthenticationForm()
# -------------------------------------------
    tax = 0
    grand_total = 0

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total) / 100
        grand_total = tax + total

    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
    }
# -------------------------------------------
    return render(request,'place_order.html',context)

# def Cart(request):
#     return render(request,'cart.html')

# def Store(request):
#     return render(request,'Store.html')

def Dashboard(request):
    return render(request,'dashboard.html')

def order_com(request):
    return render(request,'order_complate.html')

def place_order(request):
    return render(request,'place_order.html')

# def product_detail(request):
#     return render(request,'product_details.html')

def serach_result(request):
    return render(request,'serach_result.html')

def logouts(request):
    logout(request)
    return render(request,'Signin.html')