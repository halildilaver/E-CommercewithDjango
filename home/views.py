from django.shortcuts import render

from product.models import Category,Product


def index(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = \
        {
        'category': category,
        'products': products,
        }
    return render(request, 'index.html', context)
