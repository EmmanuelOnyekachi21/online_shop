from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    """
    form that allows the user to select a quantity.
    """
    
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )
    
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )