from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.
def product_list(request, category_slug=None):
    """View to display a list of products, optionally filtered by a category.

    Args:
        request (HttpRequest): The HTTP request object.
        category_slug (str, optional): The slug of the category,
                                       to filter products by. Defaults to None
    """
    category = None
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
    """View to display the details of a specific product.

    Args:
        request (HttpRequest): The Http request object.
        id (int): The ID of the product.
        slug (str): The slug of the product
    """
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'shop/product/detail.html', context)