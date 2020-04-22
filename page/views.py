from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count
from .models import PriceList,Orders,OrderTotalPrice,Users
from .form import ProductForm

# Create your views here.
def index(request):
	orders = Orders.objects.filter(status =1)
	order =orders.order_by('-order_date')
	od = order.values('order_number','user_id','order_date').distinct()
	context = {
	'order' : od,
	#'prod' : product,
	}
	return render(request,'index.html', context)

def users(request):
	users = Users.objects.all()
	
	context = {
	'users' : users,
	#'prod' : product,
	}
	return render(request,'users.html', context)		
def completedorder(request):
	orders = Orders.objects.filter(status =0)
	order =orders.order_by('-order_date')
	od = order.values('order_number','user_id','order_date').distinct()
	context = {
	'order' : od,
	#'prod' : product,
	}
	return render(request,'completedorder.html', context)		

def products(request):
	#product = get_object_or_404(PriceList,id=id)
	obj =PriceList.objects.all()
	context = {
	'obj' : obj,
	#'prod' : product,
	}
	return render(request,'products.html', context)	

def Orderspending(request, id):
	obj = Orders.objects.all().filter(order_number=id)
	total = OrderTotalPrice.objects.all().filter(order_number=id)
	#obj = get_object_or_404(Orders,order_number=id)
	context = {
	'object':obj,
	'total':total
	}
	return render(request,'orders.html',context)

def updateorderstatus(request,id):
	product =Orders.objects.filter(order_number=id)
	for i in product:
		i.status = 0
		i.save()
        
        
	
    
	return redirect(reverse("main"))
 
def addproducts(request):
	title = 'Create'
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context={
	'form': form,
	'title':title
	}
	
	return render(request,'addproduct.html', context)

def updateproducts(request,id):
	title = 'Update'
	product = PriceList.objects.get(id=id)
	form = ProductForm(request.POST or None,instance = product)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return redirect(reverse("products", kwargs={
				'id':form.instance.id
				}))
	
	
		
	context={
	'form':form,
	'title':title
	}
	return render(request,'addproduct.html', context)

def product_delete(request, id):
	obj = get_object_or_404(PriceList,id=id)
	obj.delete()
    
	return redirect(reverse("products"))  	



  	

  

    	