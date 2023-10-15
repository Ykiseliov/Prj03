from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']

class ProductFilterForm(forms.Form):
    # Добавляем поля для фильтрации, если нужно
    name = forms.CharField(max_length=100, required=False)

class ProductPhotoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['photo']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['products', 'client']

    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True  # Сделать поле products обязательным
    )
