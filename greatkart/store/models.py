from django.db import models as m
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(m.Model):
    product_name=m.CharField(max_length=50,unique=True)
    slug=m.SlugField(max_length=50,unique=True)
    description=m.TextField(max_length=500,blank=True)
    price=m.IntegerField()
    images=m.ImageField(upload_to="Photos/Products")
    stock=m.IntegerField()
    is_available=m.BooleanField(default=True)
    category=m.ForeignKey(Category,on_delete=m.CASCADE)
    created_date=m.DateTimeField(auto_now_add=True)
    modifed_date=m.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name
    