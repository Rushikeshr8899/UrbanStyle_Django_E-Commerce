"""
URL configuration for greatkart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('Register/',views.Register,name="Register"),
    path('Signin/',views.Signin,name="Signin"),
    path('Cart/',include('Cart.urls')),
    # path('Store/',views.Store,name="Store"),
    path('store/',include('store.urls')),                                
    path('Dashboard/',views.Dashboard,name="Dashboard"),
    path('order_com/',views.order_com,name="order_com"),
    path('place_order/',views.place_order,name="place_order"),
    # path('product_details/',views.product_details,name="product_details"),
    path('serach_result/',views.serach_result,name="serach_result"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
