from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from itertools import chain

# Create your views here.
def index(request):
    ac = Product.objects.filter(product_category='AC')
    ledtv = Product.objects.filter(product_category='LED TV')
    allprods = list(chain(ac, ledtv))



    params = {'allprods' : allprods}
    return render(request, 'shop/home.html', params)


def product_view (request, my_id):
    product = Product.objects.filter(product_id = my_id)
    return render(request, 'shop/product_view.html', {'product':product[0]})

def about(request):
    return render(request, 'shop/about.html')














