from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from itertools import chain

# Create your views here.
def index(request):
    all_products = Product.objects.all();
    ac = Product.objects.filter(product_category='AC')
    ledtv = Product.objects.filter(product_category='LED TV')
    allprods = list(chain(ac, ledtv))
    category_list = []
    for i in all_products:
        if(i.product_category not in category_list):
            category_list.append(i.product_category)
    category_list = sorted(category_list)
    params = {'allprods' : allprods, 'category_list' : category_list}
    return render(request, 'shop/home.html', params)





def product_view (request, my_id):
    product = Product.objects.filter(product_id = my_id)
    return render(request, 'shop/product_view.html', {'product':product[0]})

def about(request):
    return render(request, 'shop/about.html')

def viewall(request, my_category):
    temp = my_category
    product_cat = Product.objects.filter(product_category = my_category)
    params = {'product_cat' : product_cat, 'temp':temp}
    return render(request, 'shop/viewall.html', params)












