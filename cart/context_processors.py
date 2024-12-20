from .cart import Cart

def cart(request):
    """
    Context processor to make the shopping cart available in all templates.
    """
    return {'cart': Cart(request)}