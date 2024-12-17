from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Represents a product category in the online shop.

    Attributes:
        name (CharField): The name of the category, up to 200 characters.
        slug (SlugField): A unique slug for the category, used in URLs.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        """
        Meta options for the Category Model
        
        Attributes:
            ordering (list): Orders categories by their name.
            indexes (list): Adds an index for the name field to improve
                            query performance.
            verbose_name (str): A human-readable name for the model.
            verbose_name_plural (str): The plural form of the model name.
        """
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        """
        Returns the string representation of the category.

        Returns:
            str: The name of the category.
        """
        return self.name


class Product(models.Model):
    """
    Represents a product in the online shop.

    Attributes:
        category (ForeignKey): A foreign key linking the product to a category.
        name (CharField): The name of the product, up to 200 characters.
        slug (SlugField): A unique slug for the product, used in URLs.
        image (ImageField): An optional image of the product, stored in a dated directory.
        description (TextField): A detailed description of the product.
        price (DecimalField): The price of the product, with up to 10 digits and 2 decimal places.
        available (BooleanField): Indicates if the product is available for purchase.
        created (DateTimeField): The timestamp when the product was created.
        updated (DateTimeField): The timestamp when the product was last updated.
    """
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(
        upload_to='products/%Y/%M/%d',
        blank=True
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta options for the Product model.

        Attributes:
            ordering (list): Orders products by their name.
            indexes (list): Adds indexes for faster querying on specific fields.
        """
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        
    def __str__(self):
        """
        Returns the string representation of the product.

        Returns:
            str: The name of the product.
        """
        return self.name