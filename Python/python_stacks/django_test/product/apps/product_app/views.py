from django.shortcuts import render
from .models import Products
# Create your views here.
def index(request):
    Products.objects.create(name='potato',description='veggie',weight=2,price=3,cost=1.5,category ='vegetable')
    Products.objects.create(name='kiwi',description='fruit',weight=2,price=3,cost=1.5,category ='fruits')
    Products.objects.create(name='sponge',description='cleaner',weight=2,price=3,cost=1.5,category ='cleaning')
    product = Products.objects.all()
    for item in product:
        print item.name, item.description, item.weight, item.price, item.cost, item.category
    return render(request, "product_app/index.html")
