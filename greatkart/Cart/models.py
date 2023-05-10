from django.db import models as m
from store.models import Product
from django.db.models import Q
# Create your models here.

class Cart(m.Model):
    cart_id=m.CharField(max_length=200,blank=True)
    date_added=m.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(m.Model):
    product=m.ForeignKey(Product,on_delete=m.CASCADE)
    cart=m.ForeignKey(Cart,on_delete=m.CASCADE)
    quantity=m.IntegerField()
    is_active=m.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return self.product