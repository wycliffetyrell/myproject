"""dash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from page.views import index, products,addproducts,updateproducts,Orderspending,product_delete,updateorderstatus,completedorder,users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),
    path('products/', products, name ='products'),
    path('orders/<str:id>/',Orderspending,name='orders-detail'),
    path('orders/<str:id>/update',updateorderstatus,name='orders-update'),
    path('completed/',completedorder,name='orders-complete'),
    path('addproducts/', addproducts),
    path('products/<int:id>/update', updateproducts, name='product-update'),
    path('products/<int:id>/delete', product_delete, name='product-delete'),
    path('users/',users,name='user'),
   

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
