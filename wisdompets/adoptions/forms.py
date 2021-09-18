from .models import products
from bootstrap_modal_forms.forms import BSModalModelForm

class ProductModelForm(BSModalModelForm):
    class Meta:
        model = products
        fields = ['product_name', 'category_name', 'description']