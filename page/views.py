from django.shortcuts import render, get_object_or_404
from item.models import *
#from openpyxl import load_workbook
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from bs4 import BeautifulSoup
# import requests
# import urllib.request
# from django.core.files.base import ContentFile

def index(request):
    all_categories = Category.objects.filter(is_active=True, is_in_index_catalog=True)
    banners = Banner.objects.filter(at_home_page=True, is_active=True)
    return render(request, 'page/index.html', locals())


def search(request):
    all_categories = Category.objects.filter(is_active=True)
    print(request.POST)
    breadcrumb_item = f'Результаты поиска по запросу: {request.POST.get("query")}'
    items = Item.objects.filter(name_lower__contains=request.POST.get("query").lower())
    return render(request, 'page/items_page.html', locals())

def register(request):
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/register.html', locals())
def login(request):
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/login.html', locals())
def sale(request):
    all_categories = Category.objects.filter(is_active=True)
    breadcrumb_item = f'Товары со скидками'
    items = Item.objects.filter(discount__gt=0)
    banners = Banner.objects.filter(at_sale_page=True,is_active=True)
    show_banner = True
    return render(request, 'page/items_page.html', locals())

def manufactor(request,manufactor_slug):
    all_categories = Category.objects.filter(is_active=True)
    manufactor = Manufactor.objects.get(name_slug=manufactor_slug)

    breadcrumb_item = f'Товары производителя: {manufactor.name}'
    breadcrumb_return = 'Производители'
    breadcrumb_return_url = '/manufacturers/'
    items_temp = Item.objects.filter(manufactor=manufactor)
    print('items_temp',items_temp)
    count = request.GET.get('count')
    page = request.GET.get('page')
    if count:
        items_paginator = Paginator(items_temp, int(count))
        param_count = count
    else:
        items_paginator = Paginator(items_temp, 12)

    print('items_paginator', items_paginator)
    try:
        items = items_paginator.get_page(page)
    except PageNotAnInteger:
        items = items_paginator.page(1)
    except EmptyPage:
        items = items_paginator.page(items_paginator.num_pages)
    return render(request, 'page/items_page.html', locals())


def about(request):
    all_categories = Category.objects.filter(is_active=True, is_in_index_catalog=True)
    return render(request, 'page/about.html', locals())

# def cats(request):
#     wb = load_workbook(filename='C:/Users/ххх/PycharmProjects/ideaHome/cats.xlsx')
#     sheet = wb.active
#
#     max_row = sheet.max_row
#
#     max_column = sheet.max_column
#     for i in range(1, max_row + 1):
#         # worksheet.write('A{}'.format(row), cat_id)
#         # worksheet.write('B{}'.format(row), cat_name)
#         # worksheet.write('C{}'.format(row), cat_parent_id)
#         # worksheet.write('D{}'.format(row), cat_description)
#         # worksheet.write('E{}'.format(row), cat_img)
#         # worksheet.write('F{}'.format(row), cat_title)
#         # worksheet.write('G{}'.format(row), cat_keywords)
#         # worksheet.write('H{}'.format(row), cat_meta_description)
#         old_id=sheet.cell(row=i, column=1).value
#         cat_name=sheet.cell(row=i, column=2).value
#         cat_parent_id=sheet.cell(row=i, column=3).value
#         try:
#             cat_description=sheet.cell(row=i, column=4).value.replace('_x000D_','')
#         except:
#             cat_description = sheet.cell(row=i, column=4).value
#         cat_img=sheet.cell(row=i, column=5).value
#         cat_title=sheet.cell(row=i, column=6).value
#         cat_keywords=sheet.cell(row=i, column=7).value
#         cat_meta_description=sheet.cell(row=i, column=8).value
#         # if cat_parent_id ==0:
#         #     Category.objects.create(old_id=old_id,name=cat_name,description=cat_description,image='images/catalog/categories/'+cat_img,
#         #                             page_title=cat_title,page_description=cat_meta_description,page_keywords=cat_keywords)
#         if cat_parent_id != 0:
#             cat = Category.objects.get(old_id=cat_parent_id)
#             SubCategory.objects.create(old_id=old_id, name=cat_name, description=cat_description, category=cat,
#                                     page_title=cat_title, page_description=cat_meta_description,
#                                     page_keywords=cat_keywords)
#     return render(request, 'page/about.html', locals())
#
#
#
# def manuf(request):
#     wb = load_workbook(filename='C:/Users/ххх/PycharmProjects/ideaHome/manuf.xlsx')
#     sheet = wb.active
#
#     max_row = sheet.max_row
#
#     max_column = sheet.max_column
#     for i in range(1, max_row + 1):
#         # worksheet.write('A{}'.format(row), cat_id)
#         # worksheet.write('B{}'.format(row), cat_name)
#         # worksheet.write('C{}'.format(row), cat_img)
#         # worksheet.write('D{}'.format(row), cat_title)
#         # worksheet.write('E{}'.format(row), cat_keywords)
#         # worksheet.write('F{}'.format(row), cat_meta_description)
#         old_id=sheet.cell(row=i, column=1).value
#         name=sheet.cell(row=i, column=2).value
#         img=sheet.cell(row=i, column=3).value
#         cat_title=sheet.cell(row=i, column=4).value
#         cat_keywords=sheet.cell(row=i, column=5).value
#         cat_meta_description=sheet.cell(row=i, column=6).value
#
#         Manufactor.objects.create(old_id=old_id, name=name, image='images/catalog/manufacturers/'+img,
#                                     page_title=cat_title, page_description=cat_meta_description,
#                                     page_keywords=cat_keywords)
#     return render(request, 'page/about.html', locals())
#
# def itemm(request):
#     wb = load_workbook(filename='C:/Users/ххх/PycharmProjects/ideaHome/items.xlsx')
#     sheet = wb.active
#
#     max_row = sheet.max_row
#
#     max_column = sheet.max_column
#     for i in range(1, max_row + 1):
#         # worksheet.write('A{}'.format(row), item_id)
#         # worksheet.write('B{}'.format(row), item_cat_id)
#         # worksheet.write('C{}'.format(row), item_name)
#         # worksheet.write('D{}'.format(row), item_articul)
#         # worksheet.write('E{}'.format(row), item_description)
#         # worksheet.write('F{}'.format(row), item_manufactor)
#         # worksheet.write('G{}'.format(row), item_unit)
#         # worksheet.write('H{}'.format(row), item_price)
#         # worksheet.write('I{}'.format(row), item_img_main)
#         # worksheet.write('J{}'.format(row), item_img_add)
#         # worksheet.write('K{}'.format(row), item_title)
#         # worksheet.write('L{}'.format(row), item_keywords)
#         # worksheet.write('M{}'.format(row), item_meta_description)
#         old_id=sheet.cell(row=i, column=1).value
#         item_cat_id=sheet.cell(row=i, column=2).value
#         item_name=sheet.cell(row=i, column=3).value
#         item_articul=sheet.cell(row=i, column=4).value
#         try:
#             item_description = sheet.cell(row=i, column=5).value.replace('_x000D_', '')
#         except:
#             item_description = sheet.cell(row=i, column=5).value
#         item_manufactor = sheet.cell(row=i, column=6).value
#         item_unit = sheet.cell(row=i, column=7).value
#         item_price = sheet.cell(row=i, column=8).value
#         item_img_main = sheet.cell(row=i, column=9).value
#         item_img_add = sheet.cell(row=i, column=10).value
#         item_title = sheet.cell(row=i, column=11).value
#         item_keywords = sheet.cell(row=i, column=12).value
#         item_meta_description = sheet.cell(row=i, column=13).value
#         cat= None
#         subcat = None
#
#
#         try:
#             cat = Category.objects.get(old_id=item_cat_id)
#
#         except:
#             subcat = SubCategory.objects.get(old_id=item_cat_id)
#
#
#         try:
#             manufactor = Manufactor.objects.get(old_id=item_manufactor)
#         except:
#             manufactor=None
#         print(manufactor)
#         print(old_id)
#         if item_img_main:
#             item_first_big_img= item_img_main.split('|')[0]
#             item_first_small_img = item_img_main.split('|')[2]
#         else:
#             item_first_big_img = None
#             item_first_small_img = None
#         item = None
#         if cat:
#             item = Item.objects.create(manufactor=manufactor,category=cat, name=item_name,price=item_price,article=item_articul,
#                                        units=item_unit,old_id=old_id,description=item_description,
#                                        page_title=item_title,page_description=item_meta_description,page_keywords=item_keywords)
#         if subcat:
#             catt = subcat.category
#             item = Item.objects.create(manufactor=manufactor,category=catt, subcategory=subcat, name=item_name, price=item_price, article=item_articul,
#                                        units=item_unit, old_id=old_id, description=item_description,
#                                        page_title=item_title, page_description=item_meta_description,
#                                        page_keywords=item_keywords)
#         if item_img_main:
#             ItemImage.objects.create(item=item,image='images/catalog/items/'+item_first_big_img,image_small='/media/images/catalog/items/'+item_first_small_img)
#         if item_img_add:
#             for img in item_img_add.splitlines():
#                 item_big_img = item_img_main.split('|')[0]
#                 item_small_img = item_img_main.split('|')[1]
#                 ItemImage.objects.create(item=item, image='images/catalog/items/'+item_big_img, image_small='/media/images/catalog/items/'+item_small_img)
#
#
#     return render(request, 'page/about.html', locals())

def contacts(request):
    # from bs4 import BeautifulSoup
    # urls = ['https://decor-dizayn.ru/catalog/tsvetnaya-lepnina/tsvetniye_plintusy-/',
    #
    #
    #
    #         ]
    # for url in urls:
    #     req = requests.get(url)
    #     soup = BeautifulSoup(req.content, 'html.parser')
    #     all_cards = soup.find_all("div", class_="sec_card")
    #     for card in all_cards:
    #         # print(card)
    #         # print(card.find('div', class_="card_price").text.strip().split(' ')[0].split('.')[0])
    #         img = card.find('a', class_="sec_crad-pic")['href']
    #         name = card.find('a', class_="card_name").text.strip()
    #         art = card.find('div', class_="card_art").text.strip().split(' ')[1]
    #         description = card.find('div', class_="card_prop").decode_contents()
    #         price = int(card.find('div', class_="card_price").find('s').text.strip().replace(' руб.','').split('.')[0].replace(' ',''))
    #         print(price)
    #         item = Item.objects.create(category_id=3,
    #                                    subcategory_id=54,
    #                                    manufactor_id=20,
    #                                    name=name,
    #                                    price=price,
    #                                    article=art,
    #                                    description=description)
    #         # urllib.request.urlretrieve(f'https://decor-dizayn.ru/{img}', f'D:/temp/dicir/{art}.jpg')
    #
    #         # content = urllib.request.urlretrieve(f'https://decor-dizayn.ru{img}')
    #         try:
    #             response = requests.get(f'https://decor-dizayn.ru{img}')
    #             item_img = ItemImage()
    #             item_img.item=item
    #             item_img.image.save(f'{art}.jpg',ContentFile(response.content),save=True)
    #             item_img.save()
    #         except:
    #             print('error')
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/contacts.html', locals())


def delivery(request):
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/delivery.html', locals())


def manufacturers(request):
    all_categories = Category.objects.filter(is_active=True)
    all_manufacturers = Manufactor.objects.all()
    return render(request, 'page/manufacturers.html', locals())

def catalog(request):
    all_categories = Category.objects.all()
    return render(request, 'page/catalog.html', locals())


def manufacturers_cat(request,slug):
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/manufacturers.html', locals())



def category(request, category_slug):
    all_categories = Category.objects.filter(is_active=True)
    category = Category.objects.get(name_slug=category_slug)

    # remove_items = Item.objects.filter(category_id=21)
    # print(remove_items)
    # for item in remove_items:
    #     item.category_id=10
    #     item.save()
    items_qs = Item.objects.filter(category=category,is_active=True)
    items = items_qs
    manufactors = category.manufactor.all()
    qs_filtered = False
    search_res = False
    count = request.GET.get('count')
    page = request.GET.get('page')
    order = request.GET.get('order')
    filter_manufactor = request.GET.get('manufactor')
    search_q = request.GET.get('search')


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

    if count:
        items_paginator = Paginator(items, int(count))
        param_count = count
    else:
        items_paginator = Paginator(items, 18)

    print('items_paginator',items_paginator)
    try:
        items = items_paginator.get_page(page)
    except PageNotAnInteger:
        items = items_paginator.page(1)
    except EmptyPage:
        items = items_paginator.page(items_paginator.num_pages)

    return render(request, 'page/category.html', locals())

def subcategory(request, category_slug, subcategory_slug):
    all_categories = Category.objects.filter(is_active=True)
    category = Category.objects.get(name_slug=category_slug)
    subcategory = SubCategory.objects.get(name_slug=subcategory_slug)
    items_qs = Item.objects.filter(subcategory=subcategory,is_active=True)
    items = items_qs
    manufactors = subcategory.manufactor.all()
   # manufactors = subcategory.manufactor_set.all()
    qs_filtered = False
    search_res = False
    count = request.GET.get('count')
    page = request.GET.get('page')
    order = request.GET.get('order')
    filter_manufactor = request.GET.get('manufactor')
    search_q = request.GET.get('search')

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
    if count:
        items_paginator = Paginator(items, int(count))
        param_count = count
    else:
        items_paginator = Paginator(items, 18)

    print('items_paginator', items_paginator)
    try:
        items = items_paginator.get_page(page)
    except PageNotAnInteger:
        items = items_paginator.page(1)
    except EmptyPage:
        items = items_paginator.page(items_paginator.num_pages)


    return render(request, 'page/category.html', locals())

def item_page(request,category_slug,item_slug,subcategory_slug=None):
    if subcategory_slug:
        subcategory = get_object_or_404(SubCategory, name_slug=subcategory_slug)
    category = get_object_or_404(Category, name_slug=category_slug)
    all_categories = Category.objects.filter(is_active=True)

    item = get_object_or_404(Item, name_slug=item_slug)
    item.views += 1
    item.save()

    if subcategory_slug:
        recomended_items = Item.objects.filter(subcategory=subcategory,views__gt=10).order_by('-views')
    else:
        recomended_items = Item.objects.filter(category=category, views__gt=20).order_by('-views')

    filter_qs(1,None,{'dsf':'sada'})
    return render(request, 'page/item.html', locals())

def filter_qs(qs,*args,**kwargs):
    print('filter')
    print(qs)
    print(**kwargs)

def checkout(request):
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/checkout.html', locals())
