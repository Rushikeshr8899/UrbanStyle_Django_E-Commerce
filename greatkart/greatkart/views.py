from django.http import HttpResponse
from django.shortcuts import render
from category.models import Category
from store.models import Product

def Home(request):
    products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.all()  # select * from Category
    context = {'products': products, 'categories': categories}
    return render(request, 'home.html', context)

def Register(request):
    return render(request,'Register.html')

def Signin(request):
    return render(request,'Signin.html')

def Cart(request):
    return render(request,'cart.html')

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

