from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','price','stock','category')
    prepopulated_fields={'slug': ("product_name",)}
    list_display_links=('product_name','price','stock','category')


admin.site.register(Product,ProductAdmin)
