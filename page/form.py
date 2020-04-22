from django import forms

from .models import PriceList

class ProductForm(forms.ModelForm):
	class Meta:
		model = PriceList
		fields = [
			'product_name',
			'product_size',
			'product_price'

		]


	