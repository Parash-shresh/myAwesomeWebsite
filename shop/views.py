from django.http import HttpResponse
from django.shortcuts import render

from shop.models import Product

# Create your views here.
def shopIndex(request):
    return HttpResponse("from ShopIndex")
def index(request):
    return render(request, 'shop/index.html')

# def about(request):
#     return render(request,'shop/about.html')

def search(request):
    return HttpResponse("we create serach")

def productView(request):
    return HttpResponse("we create productView")

def checkout(request):
    return HttpResponse("we create checkout")

def contact(request):
    return HttpResponse("we create contact")

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
def about(request):
    objects = Product.objects.all()
    context = {
            'objects' : objects
            }
    return render(request,'shop/about.html',context)