from django.shortcuts import render,redirect
from .models import Cart
# Create your views here.
from products.models import Product


def cart_home(request):
	cart_obj,new_obj = Cart.objects.new_or_get(request)
	args = { "cart": cart_obj }
	return render(request,"carts/cart_home.html",args)

def cart_update(request):
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("Show Message to user, Product in gone?")
			return redirect("cart:home")
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)

		request.session['cart_items'] = cart_obj.products.count()

	#return redirect(product_obj.get_absolute_url()):home
	return redirect("cart:home")