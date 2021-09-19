from .models import products
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm

class ProductModelForm(BSModalModelForm):
    class Meta:
        model = products
        fields = ['product_name', 'category_name', 'description']

class Add_Product(forms.Form):
    product_name = forms.CharField(max_length=255)
    category_name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)

class Update_Product(forms.ModelForm):
    product_name = forms.CharField(max_length=255)
    category_name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    django_admin_side = forms.CharField(max_length=255)
    class Meta:
        model = products
        fields = ('product_name', 'category_name', 'description', 'django_admin_side')
class Search_by_category(forms.ModelForm):
    category_name = forms.CharField(max_length=255)