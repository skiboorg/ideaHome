from django.shortcuts import render, get_object_or_404
from item.models import *

def index(request):
    all_categories = Category.objects.filter(is_active=True, is_in_index_catalog=True)
    return render(request, 'page/index.html', locals())


def about(request):
    return render(request, 'page/about.html', locals())


def contacts(request):
    return render(request, 'page/contacts.html', locals())


def delivery(request):
    return render(request, 'page/delivery.html', locals())


def manufacturers(request):
    return render(request, 'page/manufacturers.html', locals())


def manufacturers_cat(request,slug):
    return render(request, 'page/manufacturers.html', locals())



def category(request, category_slug):
    all_categories = Category.objects.filter(is_active=True)
    category = Category.objects.get(name_slug=category_slug)
    items_qs = Item.objects.filter(category=category)
    items = items_qs
    manufactors = category.get_all_manufactors()
    qs_filtered = False
    search_res = False

    order = request.GET.get('order')
    filter_manufactor = request.GET.get('manufactor')
    search_q = request.GET.get('q')


    if search_q:
        items = items_qs.filter(name_lower__contains=search_q.lower())
        search_res = True
        param_search = search_q

    if filter_manufactor:
        if search_res:
            items = items.filter(manufactor__name_slug=filter_manufactor)
        else:
            items = items_qs.filter(manufactor__name_slug=filter_manufactor)
        qs_filtered = True
        param_manufactor = filter_manufactor

    if order == 'price_gte':
        if qs_filtered or search_res:
            items = items.order_by('-price')
        else:
            items = items_qs.order_by('-price')
        param_order = order

    if order == 'price_lte':
        if qs_filtered or search_res:
            items = items.order_by('price')
        else:
            items = items_qs.order_by('price')
        param_order = order

    if order == 'name_az':
        if qs_filtered or search_res:
            items = items.order_by('name')
        else:
            items = items_qs.order_by('name')
        param_order = order

    if order == 'name_za':
        if qs_filtered or search_res:
            items = items.order_by('-name')
        else:
            items = items_qs.order_by('-name')
        param_order = order
    return render(request, 'page/category.html', locals())

def subcategory(request, category_slug, subcategory_slug):
    all_categories = Category.objects.filter(is_active=True)
    category = Category.objects.get(name_slug=category_slug)
    subcategory = SubCategory.objects.get(name_slug=subcategory_slug)
    items_qs = Item.objects.filter(subcategory=subcategory)
    items = items_qs
    manufactors = subcategory.manufactor_set.all()
    qs_filtered = False
    search_res = False

    order = request.GET.get('order')
    filter_manufactor = request.GET.get('manufactor')
    search_q = request.GET.get('q')

    if search_q:
        items = items_qs.filter(name_lower__contains=search_q.lower())
        search_res = True
        param_search = search_q

    if filter_manufactor:
        if search_res:
            items = items.filter(manufactor__name_slug=filter_manufactor)
        else:
            items = items_qs.filter(manufactor__name_slug=filter_manufactor)
        qs_filtered = True
        param_manufactor = filter_manufactor

    if order == 'price_gte':
        if qs_filtered or search_res:
            items = items.order_by('-price')
        else:
            items = items_qs.order_by('-price')
        param_order = order

    if order == 'price_lte':
        if qs_filtered or search_res:
            items = items.order_by('price')
        else:
            items = items_qs.order_by('price')
        param_order = order

    if order == 'name_az':
        if qs_filtered or search_res:
            items = items.order_by('name')
        else:
            items = items_qs.order_by('name')
        param_order = order

    if order == 'name_za':
        if qs_filtered or search_res:
            items = items.order_by('-name')
        else:
            items = items_qs.order_by('-name')
        param_order = order

    return render(request, 'page/category.html', locals())

def item_page(request,category_slug,item_slug,subcategory_slug=None):
    if subcategory_slug:
        subcategory = get_object_or_404(SubCategory, name_slug=subcategory_slug)
    category = get_object_or_404(Category, name_slug=category_slug)


    item = get_object_or_404(Item, name_slug=item_slug)

    filter_qs(1,None,{'dsf':'sada'})
    return render(request, 'page/item.html', locals())

def filter_qs(qs,*args,**kwargs):
    print('filter')
    print(qs)
    print(**kwargs)