from django.shortcuts import render
from .models import Product, Category, Tag

def product_list(request):
    products = Product.objects.all()
    query = request.GET.get("q")
    category = request.GET.get("category")
    tag = request.GET.get("tag")

    if query:
        products = products.filter(description__icontains=query)
    if category:
        products = products.filter(category__id=category)
    if tag:
        products = products.filter(tags__id=tag)

    return render(request, "catalog/product_list.html", {
        "products": products,
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
    })
