from django.http import Http404
from django.shortcuts import render

from product.models import Product


def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'detail.html', {'product': product})