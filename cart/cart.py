from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    """
    A class to represent the shopping cart.

    The Cart class manages the items in the shopping cart, including adding, 
    removing, and updating product quantities. It also computes the total cost 
    and allows for iteration over the items in the cart.

    Attributes:
        session (dict): The session dictionary to store the cart data.
        cart (dict): The dictionary representing the cart items.
    """
    
    def __init__(self, request):
        """
        Initialize the Cart.
        
        This method initializatizes the cart by fetching the cart from the session 
        or creating a new empty cart if none exists.

        Args:
            request (HttpRequest): The request object from the user session.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.

        This method either adds a new product to the cart or updates the quantity 
        of an existing product based on the override_quantity flag.

        Args:
            product (Product): The product to add to the cart.
            quantity (int, optional): The quantity to add (default is 1).
            override_quantity (bool, optional): Whether to override the
                                                  quantity (default is False).
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
            }
        
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        self.save()
    
    def save(self):
        """
        Mark the session as modified to ensure it gets saved.

        This method sets the session as modified so that the changes to the cart 
        are stored in the session.
        """
        self.session.modified = True
        
    def remove(self, product):
        """
        Remove a product from the cart.

        This method removes the product from the cart and updates the session.

        Args:
            product (Product): The product to remove from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
        
    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.

        This method retrieves the Product instances from the database and adds 
        them to the cart items for easier iteration in templates. It also adds 
        the total price for each item.

        Yields:
            dict: The cart items, including product details, quantity, and total price.
        """
        products_id = self.cart.keys()
        # Get the product objects based on the IDs in the cart
        products = Product.objects.filter(id__in=products_id)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        """
        Count all items in the cart.

        This method returns the total number of items in the cart, based on their 
        quantities.

        Returns:
            int: The total number of items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """
        Calculate the total cost of the items in the cart.

        This method calculates the total cost by summing the price of each item 
        multiplied by its quantity.

        Returns:
            Decimal: The total cost of the cart items.
        """
        return sum(
            float(item['price']) * item['quantity']
            for item in self.cart.values()
        )
        
    def clear(self):
        """
        Clear the cart by removing it from the session.

        This method deletes the cart from the session and saves the changes.
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()