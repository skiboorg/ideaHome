from django.shortcuts import render
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