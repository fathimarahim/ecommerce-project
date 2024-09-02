from django.core.handlers import exception
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.

def allprodcat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True).order_by(
            'name')  # Order by name or any other field
    else:
        products_list = Product.objects.filter(available=True).order_by('name')  # Order by name or any other field

    paginator = Paginator(products_list, 6)  # 6 products per page

    page = request.GET.get('page', '1')

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)  # Fallback to the last page

    return render(request, 'category.html', {'category': c_page, 'products': products})

def productdetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'product_list.html', {'product': product})
