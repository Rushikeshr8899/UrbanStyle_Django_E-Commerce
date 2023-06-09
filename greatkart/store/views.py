from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
from Cart.models import CartItem
from Cart.views import _cart_id


# Create your views here.


def store(request,category_name=None):
    # categories=None
    # products=None

    products=Product.objects.all().filter(is_available=True)
    products_count=products.count()
    if category_name:
        categories=get_object_or_404(Category,slug=category_name)
        products=Product.objects.all().filter(category=categories)
        products_count=products.count()

    content= {'product':products,'products_count':products_count}

    return render(request,'Store.html',content)


def product_detail(request, category_name=None, product_name=None):
    try:
        single_product = Product.objects.get(category__slug=category_name, slug=product_name)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Exception as e:
        raise e
    context = {'single_product': single_product,
               'in_cart': in_cart}
    return render(request, 'product_details.html', context)
