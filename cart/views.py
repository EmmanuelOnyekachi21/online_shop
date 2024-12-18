from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from shop.models import Product
from .forms import CartAddProductForm

# Create your views here.
@require_POST
def cart_add(request, product_id):
    """
    Add a product to the cart or update its quantity.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    """
    Remove a product from the cart
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    """
    The cart body
    """
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})