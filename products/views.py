from django.shortcuts import render
import requests
import json
from django.views.generic import ListView
from .models import Product
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

class IndexView(ListView):
    template_name = 'products/product_list.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r = requests.get('https://suppliers-api.wildberries.ru/public/api/v1/info', headers={'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjRmODE0NDA3LWI3ZWQtNDVlNS04MzgxLWNlN2QyNTcwNWRhYiJ9.7M5xJmAZEBRcoEcZukw6ae-7VamUqmPGKNzei3Zj4KQ'})
        data = r.json()
        prices = {str(item['nmId']):(int(item['price'] - item['price']*item['discount']/100)) for item in data}
        context['prices'] = prices
        return context
