from django.shortcuts import render, get_object_or_404
from item.models import *

def index(request):
    all_categories = Category.objects.filter(is_active=True, is_in_index_catalog=True)
    return render(request, 'page/index.html', locals())

def category(request, category_slug):
    all_categories = Category.objects.filter(is_active=True)
    category = Category.objects.get(name_slug=category_slug)
    items = Item.objects.filter(category=category)
    manufactors = category.get_all_manufactors()

    print(items)
    print(manufactors)
    return render(request, 'page/category.html', locals())

def item_page(request,category_slug,subcategory_slug,item_slug):
    category = get_object_or_404(Category, name_slug=category_slug)
    subcategory = get_object_or_404(SubCategory, name_slug=subcategory_slug)
    print(subcategory.name)
    item = get_object_or_404(Item, name_slug=item_slug)
    return render(request, 'page/item.html', locals())