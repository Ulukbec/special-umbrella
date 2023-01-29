from django.shortcuts import render
from store.models import Product


# Create your views here.

def main_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == "GET":
        product = Product.objects.all()

        return render(request, 'products/products.html', context={
            'products': product
        })


def detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        return render(request, 'products/detail.html', context={
            'product': product
        })
