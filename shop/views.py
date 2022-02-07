from math import ceil #product slides show garna lai logic 
from django.http import HttpResponse
from django.shortcuts import render

from shop.models import Product

# Create your views here.
def shopIndex(request):
    return HttpResponse("from ShopIndex")

def index(request):
    #sabai product database bata line
    products = Product.objects.all()

    print(products) #this prints value from products
    
    #logic to display product slides
    n = len(products)
    nSlides = n//4 +ceil((n/4)-(n//4))

    params = {'no_of_slides': nSlides,'range': range(1,nSlides), 'product': products} #dictionary declared for passing. product ma sabai products aauxa
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')

def search(request):
    return HttpResponse("we create serach")

def productView(request):
    return HttpResponse("we create productView")

def checkout(request):
    return HttpResponse("we create checkout")

def contact(request):
    return render(request,'shop/contact.html')

def tracker(request):
    return HttpResponse("we create tracker")


    # for exercise: display product in PRODUCT model
    #/shop ko index.html template ma display garna lageko. yesko lagi tala ko code index.html ma halne  ani index() views ma dine
#      <p>
#     {% for object in objects %}
#       <h1>{{object.product_name}}</h1>
#       <b>{{object.product_desc}} </b> 
#       <br>{{object.category}}<br>
#       {{object.price}}<br>
#       {{object.product_published}} <br>
#       {{object.image}}<br>
#     {% endfor %}
#   </p>
def listProduct(request):
    objects = Product.objects.all()
    context = {
            'objects' : objects
            }
    return render(request,'shop/listProduct.html',context)