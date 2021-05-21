from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from itertools import chain
from django.core.mail import send_mail



# Create your views here.
def index(request):
    all_products = Product.objects.all();
    ac = Product.objects.filter(product_category='Air Conditioners')
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


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, phone=phone, email=email, message=message)
        contact.save()

        data = {
            'name' : name,
            'phone' : phone,
            'email' : email,
            'message' : message
        }
        message = '''
        Name : {}
        Phone : {}
        Email : {}
        Message : {}
        '''.format(data['name'], data['phone'], data['email'], data['message'])
        send_mail('Contact us website message', message, '', ['krishnaelectronicsweb@gmail.com'])

        print(data)
    return render(request, 'shop/home.html')





