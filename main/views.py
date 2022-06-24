from django.shortcuts import render
from django.http import Http404, HttpResponse
from main.models import Product

# Create your views here.
def index_page_viwe(request):
    text = 'Heloo world!'
    return HttpResponse(text)


def products_list(request):
    products = Product.objects.all()
    # print(products)
    return render(request, 'main/products_list.html', context={'products': products})


def product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        # print(product)
        return render(request, 'main/product_details.html', {'product': product})
    except Product.DoesNotExist:
        raise Http404
# prod = Product.objects.all()
# print(prod)